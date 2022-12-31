# coding:utf8


import abc

"""
描述符的别名为自动的名字;
"""


class AutoStorage:
    __count = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__count
        self.storage_name = "_{}#{}".format(prefix, index)
        cls.__count += 1

    def __get__(self, instance, owner):
        # if instance is None:
        #     return self
        # else:
        #    return getattr(instance, self.storage_name)
        return instance.__dict__.get(self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

# 描述符的继承
class Validated(abc.ABC, AutoStorage):
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        """ return validated value or raise ValueError"""

# 数量
class Quantity(Validated):
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError("value must be be>0")
        return value


class NonBlank(Validated):
    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError("value cannot be empty or blank")
        return value


class Demo(object):
    weight = AutoStorage()
    price = AutoStorage()

    def __init__(self, w, p):
        """ """
        self.weight = w
        self.price = p

    def total(self):
        return self.weight * self.price

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return "<Demo weight:{} price:{}".format(self.weight, self.price)

def test_msf():
    demo = Demo(10, 2)
    print(demo)
    print("total is {}".format(demo.total()))
    demo.set_price(8)
    print("demo obj is : {}".format(demo))
    print("totao is {}".format(demo.total()))
    print("demo's __dict__: {}".format(demo.__dict__))

test_msf()


