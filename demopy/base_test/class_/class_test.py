# -*- coding: utf-8 -*-
'''
@File    :   class_test.py
@Time    :   2021/09/21 19:54:11
'''
import sys


class A(object):
    ca = 1
    cl = []

    def __init__(self):
        self._a = 1

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def birth(self):
        return 200 - self._age

    @staticmethod
    def func_st():
        print('[%s] - ' % (sys._getframe().f_lineno), "in staticmethod function...")
        pass

    @classmethod
    def func_cls(cls, cc):
        cls.ca = cc
        print("set class ca value is : %s" % cc)
        pass

    @classmethod
    def func_append(cls, value):
        cls.cl.append(value)

    # 只读属性
    @property
    def pro_a(self):
        return 15
        pass

    @property
    def a(self):
        return self._a

    def out(self):
        print(
            "slef.ca： %s" % self.ca,
            "slef.cl： %s" % self.cl,
            "slef.a： %s" % self.a,
            end='\n',
            sep=" ||"
        )
        pass


obj = A()
# obj.out()
# obj.func_cls(100)
# for i in range(10, 20):
#     obj.func_append(i)
# obj.func_st()
# print(obj.pro_a)
# obj.out()

# print("obj.a : %s" % obj.a)


# obj.age = 30 
try:
    print("obj.age : %s" % obj.age)
except AttributeError as e:
    print("错误的属性!")

# print("obj.birth : %s" % obj.birth)
