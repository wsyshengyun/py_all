# coding:utf8
"""
测试关于函数内变量
"""

a = 10


def foo():
    """ """
    print("a is {}".format(a))


def fun():
    a = 20
    foo()


fun()  # a is 10
