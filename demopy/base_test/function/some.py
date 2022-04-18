# -*- coding: utf-8 -*-
'''
@File    :   some.py
@Time    :   2020/10/17 11:06:54
'''

from functools import wraps


def fun():
    return id(fun)


def logfunc(func):
    # @wraps
    def _inner(*args, **kwargs):
        return fun()
        # return 5

    return _inner


print(fun())
print(logfunc(fun)())


# 函数签名
def myfoo(a: 'int>0' = 80) -> str:
    """ """
    m = a + 100
    return str(m)


print(myfoo(-90))


# 仅限关键字参数
def foo(a, *, b):
    print("a is {} b is {}".format(a, b))


# foo(10, 20)  # 报错
foo(10, b=20)  # 运行ok
foo(b=10, a=20)  # 运行ok
