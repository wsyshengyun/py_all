# coding:utf8

'''
单例模式
以下代码说明:
当_instance没有对象时,构造MySigletion要进行创建对象;
创建对象要调用__init__方法,当创建了一个对象后,后面再执行MySigletion创建新的对象时,
就不会再调用__ini__方法了,因为_instance实例已经存在

即使有新的类继承MySigletion,新的类实例化时会先运行父类,当_instance存在时,也不会运行
新的类的__init__方法了.
'''


class MySigletion(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, c=5):
        self.c = c
        pass


class Brid(MySigletion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'a: {}, b:{}'.format(self.a, self.b)


s1 = MySigletion()
s2 = MySigletion()
print(s1 is s2)  # True

b1 = Brid(1, 3)
b2 = Brid(3, 4)

print(b1 is b2)  # True
print(s1 == b1)  # True
print(b1)
print(b2)


class ASigle(MySigletion): pass


class BSigle(MySigletion): pass


class A1Sigle(MySigletion): pass


a = ASigle()
b = BSigle()
a1 = A1Sigle()

a.x = 100
print(b.x, a1.x)  # !!! 100, 100
