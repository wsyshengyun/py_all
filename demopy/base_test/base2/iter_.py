# coding:utf8


class A(object):
    def __init__(self, a=2):
        """ """
        self.a = a
        self.lit = []
        self.o = {}
        self.i = 0

    def __iter__(self):
        print("__iter__")
        return iter(self.o)

    # def __next__(self):
    #     if self.i < len(self.lit):
    #         val = self.lit[i]
    #         self.i += 1
    #         return val
    #     else:
    #         raise StopIteration


def test1():
    obj = A()
    obj.lit = [1, 2, 3, 4, 5, 6]
    ltt = [3, 4, 5, 6, 7]
    dit = {'a': 1, 'b': 2, 'c': 3}
    obj.o = dit
    it = iter(obj)
    # it = obj.__iter__()
    # for k, v in it:
    #     print(k, v)
    print(next(it))
    print(next(it))
    print(next(it))


# test1()


def test2():
    class B(object):
        a = 0

        def __iter__(self):
            print("__iter__")
            return self

        def __next__(self):
            self.a += 1
            if self.a > 5:
                raise StopIteration
            return 1

    obj = B()
    it = iter(obj)    # 打印__iter__
    for i in obj:  # 打印__iter__
        print(i)
    pass


# test2()


from collections import Iterator


class C(object):

    def __init__(self):
        """ """
        self.o = {'a':1, 'b':2, 'c':3}

        result = isinstance(self, Iterator)
        print("self 创建的对象是否是一个可迭代对象: {}".format(result))

    def __iter__(self,):
        return iter(self.o)


obj = C()
it = iter(obj)
for i in obj:
    print(i)

