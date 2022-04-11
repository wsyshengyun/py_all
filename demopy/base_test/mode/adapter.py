# coding:utf-8

"""
适配器模式
有两种方式实现适配器模式
1 继承要适配的类
2 组合要适配的类的一个实例

"""


class Polygon(object):
    """a polygon class"""

    def __init__(self, *sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

    def is_valid(self):
        raise NotImplementedError

    def is_regular(self):
        side = self.sides[0]
        return all([side == x for x in self.sides[1:]])

    def area(self):
        raise NotImplementedError


import itertools


class InvalidPolygonError(Exception):
    pass


class Triangle(Polygon):

    def is_equilateral(self):
        """ 是否是一个等边三角形"""
        if self.is_valid():
            return super(Triangle, self).is_regular()

    def is_isosceles(self):

        if self.is_valid():
            combin_iter = itertools.combinations(self.sides, 2)
            for i, j in combin_iter:
                if i == j:
                    return True
        return False

    def area(self):
        p = self.perimeter() / 2
        total = p
        for side in self.sides:
            total *= abs(p - side)
        return pow(total, 0.5)

    def is_valid(self):

        perimeter = self.perimeter()
        # iter_combin = itertools.combinations(self.sides, 2)
        # for a, b in iter_combin:
        #     san = perimeter - a - b
        #     if a + b < san:
        #         raise InvalidPolygonError(str(self.__class__) + 'is invalid')
        for side in self.sides:
            total = perimeter - side
            if total <= side:
                raise InvalidPolygonError(str(self.__class__) + 'is invalid')

        return True


class Rectangle(Polygon):

    def is_square(self):
        if self.is_valid():
            return self.is_regular()

    def is_valid(self):

        if len(self.sides) != 4: return False

        for a, b in [(0, 2), (1, 3)]:
            if self.sides[a] != self.sides[b]:
                return False
        return True

    def area(self):

        if self.is_valid():
            return self.sides[0] * self.sides[1]


class TriangleA(object):

    def __init__(self, *sides):

        self.polygon = Polygon(*sides)

    def perimeter(self):

        return self.polygon.perimeter()

    def is_valid(f):  # 不带self参数
        """
        !!!
        :return:
        """

        def inner(self, *arg):

            perimeter = self.perimeter()
            for side in self.polygon.sides:
                total = perimeter - side
                if side >= total:
                    raise (InvalidPolygonError(str(self.__class__) + "invalid"))
            result = f(self, *arg)
            return result

        return inner

    @is_valid
    def is_regular(self):
        return self.polygon.is_regular()

    @is_valid
    def is_equilateral(self):

        return self.polygon.is_regular()

    @is_valid
    def is_isosceles(self):

        for a, b in itertools.combinations(self.polygon.sides, 2):
            if a == b:
                return True
        return False

    def area(self):
        p = self.polygon.perimeter() / 2
        total = p
        for side in self.polygon.sides:
            total *= abs(p - side)
        return pow(total, 1 / 2)


t1 = TriangleA(20, 20, 20)
print(t1.is_valid(), t1.is_regular(), t1.is_equilateral(), t1.is_isosceles())
print(t1.perimeter(), t1.area())

t1 = Triangle(20, 10, 30)
# print(t1.is_valid())  # 报错, 无效的三角形
