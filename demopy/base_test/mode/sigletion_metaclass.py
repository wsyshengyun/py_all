# coding:utf-8

class MetaSingleton(type):

    def __init__(cls, *args):
        print(cls, "__init__ method is called with args", args)
        type.__init__(cls, *args)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls, "creating instance", args, kwargs)
        return cls.instance


class SingletonM(metaclass=MetaSingleton):
    pass


class Sa(SingletonM):

    def __init__(self, a=10):
        self.a = a

    def __str__(self):
        return "<a is {}".format(self.a)


obj = Sa(20)
s2 = Sa(40)
print(obj is s2)
print(obj)
print(s2)
