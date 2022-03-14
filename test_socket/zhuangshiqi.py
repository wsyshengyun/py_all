# -*- coding: utf-8 -*-
'''
@File    :   zhuangshiqi.py
@Time    :   2021/09/21 11:35:09

关于python装饰器
'''

import sys
from functools import wraps
#=====================================定义一个装饰器=======================================
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('[%s] - '% (sys._getframe().f_lineno),"123")
        return func(*args, **kwargs)
    
    return wrapper


#=====================================带参数的装饰器=======================================
def decorator_parameter(value):
    def inner_2(func):
        @wraps(func) 
        def inner_3(*args, **kwargs):
            print(value)
            return func(*args, **kwargs)
        return inner_3

    return inner_2





#=====================================类装饰器=======================================
class DecoratorClass(object):
    def __init__(self, func):
        print('[%s] - '% (sys._getframe().f_lineno),"我是类装饰器的方法__init__")
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


# 利用装饰器实现缓存的功能
class Cache(object):
    __cache ={}

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        dit_cache = Cache.__cache
        if self.func.__name__ in dit_cache :
            return dit_cache.get(self.func.__name__)
        else:
            value = self.func(*args, **kwargs) 
            dit_cache[self.func.__name__] = value 
            return value


#=====================================main()=======================================
# @decorator_parameter("456")
# @decoator
@DecoratorClass
def say_hello():
    """ say hello function"""
    print('[%s] - '% (sys._getframe().f_lineno),"同学你好！")
    

import time 
@Cache
def test_cache():
    time.sleep(3) 
    return "我是计算结果"

def main():
    # say_hello()
    # print(say_hello.__name__)
    # print(say_hello.__doc__)

    # 装饰器实际调用  
    # decorator_parameter("456")(say_hello)()

    # 缓存测试
    start = time.time()
    print('[%s] - '% (sys._getframe().f_lineno),test_cache())
    end = time.time() 
    print("运行时间为： %.4s 秒" % (end-start))

    start = time.time()
    print('[%s] - '% (sys._getframe().f_lineno),test_cache())
    end = time.time()
    print("第二次运行时间为： %.4s 秒" % (end-start))


    pass

main()


