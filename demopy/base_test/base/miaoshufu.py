# coding:utf8 

class Quantity(object):
    def __init__(self, name):
        self.storage_name = name

    def __set__(self, instance, value):

        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise (ValueError(" value must be > 0"))


class QuantityA(object):
    count = 0

    def __init__(self):
        cls = self.__class__
        index = cls.count
        prefix = cls.__name__
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.count += 1
        pass

    def __get__(self, instance, owner):
        """ owner 为instance的类"""
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            # instance.__dict__[self.storage_name] = value
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError("value must be >0")


class LineItem(object):
    weight = Quantity("weight")
    price = Quantity("price")

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def set_price(self, value=2):
        self.price = value


class A(object):
    count = 1

    def __init__(self, a):
        cls = self.__class__
        self.a = a
        cls.count += 1

    @classmethod
    def print_count(cls):
        print(cls.count)


class LineItemA(LineItem):
    price = QuantityA()
    weight = QuantityA()
    pass


truff = LineItemA('Whit0 truffle', 100, 1)
truff.set_price()
truff.price

# obj = None
# for i in range(5):
#     obj = A(5)
# obj.print_count()
#
#
# class B:
#     a1 = A(5)
#     a2 = A(6)


# b = B()
# b2 = B()
# obj.print_count()
