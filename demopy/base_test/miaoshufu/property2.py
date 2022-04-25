# coding:utf-8  

""" property重写 """


class TestProperty(object):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        # print("__init__ TestProperty ")
        print('__init__')
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc
        # self.print_param()

    def print_param(self):
        print("[ fget:{}, fset:{}, fdel:{}, doc:{} ] ".format(
            self.fget, self.fset, self.fdel, self.__doc__
        ))
        pass

    def __get__(self, obj, objtype=None):
        print("in __get__")
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError
        return self.fget(obj)

    def __set__(self, obj, value):
        print("in __set__")
        if self.fset is None:
            raise AttributeError
        self.fset(obj, value)

    def __delete__(self, obj):
        print("in __delete__")
        if self.fdel is None:
            raise AttributeError
        self.fdel(obj)

    def getter(self, fget):
        print("in getter")
        return type(self)(fet, self.fset, self.fdel, self.__doc__)

    def delete(self, fdel):
        print("in delete")
        return type(self)(self.fget, self.fset, fdel, self.__doc__)

    def setter(self, fset):
        print('.....setter.....')
        # print("in setter, and type(self) : [{}]".format(type(self)))
        return type(self)(self.fget, fset, self.fdel, self.__doc__)


class Student:
    def __init__(self, name):
        print('in Student __init__')
        self.name = name

    @TestProperty
    def math(self):
        print(id(math))
        return self._math

    # math = TestProperty(math)/
    print(id(math), type(math))
    print(id(math.fget))

    @math.setter
    def math(self, value):
        if 0 <= value <= 100:
            self._math = value
        else:
            raise ValueError("Valid value must be in [0,100]")

    print(id(math), type(math))
    print(id(math.fset))
# print('----------------')
# obj = Student('wsy') 
# print('----------------')
# obj.math = 100
# print('----------------')
# print(obj.math)
