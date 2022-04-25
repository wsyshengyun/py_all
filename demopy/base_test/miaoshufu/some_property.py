# coding:utf-8  

class someProperty(object):
    def __init__(self, fget=None, fset=None):
        print("__init__")
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        print("__get__")
        return self.fget(instance)
        """ 这里只要有区分，就不会返回一样的值
        或者比如这里区分的是instance， 不同实例返回的不一样
        或者区分描述符的标签：
        return instance.__dict__.get('naem', None)
        同一实例，不同标签描述符返回的不一样  """

    def __set__(self, instance, value):
        print("__set__")
        self.fset(instance, value)

    def setter(self, func):
        print("setter")
        self.fset = func
        return type(self)(self.fget, self.fset)


class Test(object):
    def __init__(self, a):
        print("Test __init__")
        self.a = a

    @someProperty
    def math(self):
        print("math....")
        return self._math

    @math.setter
    def math(self, value):
        print("math set...")
        if not isinstance(value, int):
            raise TypeError("typeerror")
        if not 0 < value <= 100:
            raise ValueError('value must be [0, 100]')
        self._math = value


obj = Test(2)
obj.math = 99
print(obj.math)
print("=" * 30)

obj2 = Test(3)
obj2.math = 45
print(obj.math, obj2.math)
