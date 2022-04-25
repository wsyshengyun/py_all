# coding:utf-8

class BrokenNonNegative(object):
    def __init__(self, default):
        self.value = default

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Negative value not allowed:%s" % value)
        self.value = value


class Foo(object):
    bar = BrokenNonNegative(5)

    def __init__(self, bar=0):
        self.bar = bar

    def func(slef):
        pass


# f = Foo(9)
# g = Foo(10) 
# print(f.bar, g.bar)
# print(f.bar is g.bar)
print(Foo.func)
print(Foo().func)
print(Foo.func.__get__)
