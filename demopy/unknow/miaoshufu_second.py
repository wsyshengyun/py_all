# coding:utf8
"""
对于描述符，如果一个描述符含有__get__和__set__方法
一个类含有描述符，那个这个对象在初始化的时候一定是先set， 那么这个时候其
instance的__dict__其实是什么也没有的，当instance.__dict__[name] = ...
的时候，就给空上instance的__dict__增加了key和value；

"""

class Value(object):
    def __init__(self, name=None):
        """ """
        self.name = name
        print('__int__, name is {}'.format(self.name))

    def __get__(self, instance, owner):
        print('__get__')
        return instance.__dict__.get(self.name)
        pass

    def __set__(self, instance, value):
        print('__set__, value is {}'.format(value))
        instance.__dict__[self.name] = value
        pass


class Number:
    # v1 = Value('v1')
    v1 = Value('v1')
    v2 = Value('v2')

    def __init__(self, a1=0, a2=11):
        """ """
        self.v1 = a1
        self.v2 = a2

    def __str__(self):
        return  f'<Number: v1={self.v1}, v2={self.v2}'


class Cname(object):
    def __init__(self, a=5):
        """ """
        self.a = a

    # 此函数被首先调用, 打印 item is a
    # def __getattribute__(self, item):
    #     print("__getattribute__", "item is {}".format(item))
    #     pass

    def __getattr__(self, item):
        print("__getattr__, item is {}".format(item))
        pass

    def __getitem__(self, item):
        print("__getitem__, item is {}".format(item))
        pass

    def __get__(self, instance, owner):
        print("__get__, instance is {}".format(instance))
        pass

    def __class_getitem__(cls, item):
        print("__class_getitem")
        pass

    def __getinitargs__(self):
        print("__getinitargs__")
        pass


if __name__ == '__main__':
    # n = Number(1, 9)
    # print(n)
    # n2 = Number(2)
    obj = Cname()
    print(obj.a)
