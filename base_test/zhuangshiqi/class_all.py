# coding:utf8 

from functools import wraps 
import time , functools 

class DelayFunc:
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func 

    def __call__(self, *args, **kwargs):
        print(r"Wait for {self.duration} seconds")
        time.sleep(self.duration)
        return self.func(*args, **kwargs) 


    def eager_call(self, *args, **kwargs):
        print("call without delay ")
        return self.func(*args, **kwargs) 


def delay(duration):
    return functools.partial(DelayFunc, duration) 



@delay(duration=2)
def add(a,b):
    return a+b  




# =================================================
instances = {} 
def singleton(cls):
    def get_instance(*args, **kw):
        cls_name = cls.__name__ 
        print("__1__")
        if  cls_name not in instances:
            print("__2__")
            instance = cls(*args, **kw)
            instances[cls_name] = instance 
        return instances[cls_name] 
    return get_instance 

@singleton
class User:
    _instance = None 
    def __init__(self, name):
        print("__3__")
        self.name = name 


# ====================wraps装饰器=============================
def wrapper(func):
    @wraps(func)
    def inner_functions():
        
        pass
    return inner_functions 

@wrapper
def wrapped():
    pass




# ================================================
# class decorator 
# 装饰器不带参数 
# ================================================
import functools
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print(" in func, name is :{}".format(func.__name__)) 
        print("out func") 
        return func(*args, **kw) 
    return wrapper 


@logger
def add_logger(a,b):
    return a+b  



# ================================================
# 装饰器带参数 
# ================================================
def logger_level(level):
    
    def wrapper(*args, **kw):
        print(" in func, name is :{}".format(func.__name__)) 
        print("out func") 
        return func(*args, **kw) 
    return wrapper 


@logger
def add_logger(a,b):
    return a+b  



# ================================================
# 装饰器带参数 
# ================================================
def logger_level(level):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if level == 'info':
                print(" in func, name is :{}, level = info ".format(func.__name__)) 
            else:
                print(" in func, name is :{}, level = other ".format(func.__name__)) 
            print("out func") 
            return func(*args, **kw) 
        return wrapper 
    return inner 

@logger_level('info')
def add_logger_level(a,b):
    return a + b 
    


# ================================================
# 装饰器带参数 
# ================================================
def logger_level(level):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if level == 'info':
                print(" in func, name is :{}, level = info ".format(func.__name__)) 
            else:
                print(" in func, name is :{}, level = other ".format(func.__name__)) 
            print("out func") 
            return func(*args, **kw) 
        return wrapper 
    return inner 

@logger_level('info')
def add_logger_level(a,b):
    return a + b 



# ================================================
# 类装饰器 
# ================================================
class Foo:
    def __init__(self, func):
        self.func = func
        pass

    def __call__(self, *args, **kwargs):
        print("ok")
        sum =  self.func(*args, **kwargs) 
        print("out")
        return sum 
@Foo
def test_class_param(a,b):
    return a+b




# ================================================
# 类装饰器带参数 
# ================================================

class Foo:
    def __init__(self, param):
        self.param = param
        pass

    def __call__(self, func):
        def _inner(*args, **kwargs):
            print('self.param = {}'.format(self.param))
            print("ok")
            sum =  func(*args, **kwargs) 
            print("out")
            return sum 
        return _inner
        

@Foo('sssssss')
def test_class_param_on(a,b):
    return a+b














