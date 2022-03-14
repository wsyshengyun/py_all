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