# coding:utf8
"""
测试关于函数内变量
"""

a = 10


def foo():
    """
    初始化foo的时候,已经与 global a  绑定了
    """
    print("a is {}".format(a))


def fun():
    a = 20
    foo()


fun()  # a is 10
