# coding:utf8 

import functools
import time
from functools import wraps


class DelayFunc:
    def __init__(self, duration, func):
        self.duration = duration  # 期间 duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Wait for {self.duration} seconds")
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print("call without delay ")
        return self.func(*args, **kwargs)


def delay(duration):
    return functools.partial(DelayFunc, duration)


@delay(duration=2)
def add(a, b):
    return a + b


# -----------------------------------------------------------
# 装饰器应用在单例模式
# -----------------------------------------------------------
instances = {}


def singleton(cls):
    """
    1 第一个参数 接受被装饰的对象的名字(类或函数)
    2 第一个参数为 被装饰的函数的 通用参数
    3 外函数返回内函数对象; 内函数返回被装饰函数的执行
            执行也就是: 如果是类就是  类名(参数)  如果是函数就是返回: 函数名(参数)
    """

    def get_instance(*args, **kw):  # 参数为创建被装饰的类的初始化参数
        cls_name = cls.__name__
        if cls_name not in instances:
            instance = cls(*args, **kw)
            instances[cls_name] = instance
        return instances[cls_name]  # 装饰器最终要返回被装饰函数的执行结果
        # return instance

    return get_instance  # 返回内层函数\\\\


@singleton
class User:
    _instance = None

    def __init__(self, name=None):
        self.name = name

    def print_name(self):
        print("User.name : {}".format(self.name))


# test singleton decorator
print()
print("测试装饰器应用在单例模式")
user_obj = User(name='lrf')
user_obj2 = User(name='wsy')
print("user_obj is equal user_obj2: {}".format(user_obj == user_obj2))  # True 
user_obj.print_name()  # lrf
user_obj2.print_name()  # lrf
print("class User's name : {}".format(User.__name__))  # get_instance


# ====================wraps装饰器=============================
def wrapper(func):
    @wraps(func)  # 参数是被装饰的函数
    def inner_functions():
        pass

    return inner_functions


@wrapper
def wrapped():
    pass


print("")
print("测试functools.wraps函数")
print("wrapped function's name is : {}".format(wrapped.__name__))


# ================================================
# 装饰器不带参数 
# 不带参数的装饰器是两层函数，第一层参数是被装饰的函数名字，第二层是被装饰函数的参数*args, **kwargs
# ================================================
def logger(func):
    """ 功能：打印被装饰函数的名字 """
    print("__1")

    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("__2")
        return func(*args, **kw)

    print("__3")
    return wrapper


@logger
def add_logger(a, b):
    return a + b


print("")
print("不带参数的装饰器")
print("add_logger(1,2) = {}".format(add_logger(1, 2)))
print("装饰后函数的名字是：{}".format(add_logger.__name__))


# 不带参数的装饰器
# __2
# add_logger(1,2) = 3
# 装饰后函数的名字是：add_logger
# __1
# __3


# ================================================
# 装饰器带参数 
# ================================================
def logger_level(level):
    """
    带参数的装饰器: 参数可以在最内层使用
    """

    def _inner(func):
        @functools.wraps(func)
        def __inner(*args, **kw):
            print("level is : {}".format(level))
            return func(*args, **kw)

        return __inner

    return _inner


@logger_level(level='info')
def add_logger(a, b):
    return a + b


print()
print("测试带参数的装饰器")
print("add_logger(4,5) = {}".format(add_logger(4, 5)))
print(add_logger.__name__)


# ================================================
# 类装饰器  - 不带参数
# 类装饰器和去装饰类
#  1 被装饰的对象名字 作为装饰器类的初始化参数
#  2 __call__(self, *args, **kwargs) 的参数为通用参数,此函数要返回被装饰函数的执行
# ================================================
class Foo:
    def __init__(self, func):
        self.func = func
        pass

    def __call__(self, *args, **kwargs):
        print("in __call__")
        return self.func(*args, **kwargs)


@Foo
def test_class_decorator(a, b):
    return a + b


print("")
print("test no param class-decorator")
print(test_class_decorator(4, 5))


# ================================================
# 类装饰器带参数
# 1 初始化函数的参数为 装饰器的参数
# 2 __call__的参数为 被装饰对象的名字
#     __call__还需要有内函数,参数为被装饰的对象的参数,通用参数
# ================================================

class Foo:
    def __init__(self, param):
        self.param = param

    def __call__(self, func):
        def _inner(*args, **kwargs):
            print('self.param = {}'.format(self.param))
            return func(*args, **kwargs)

        return _inner

    def par(self, *args, **kwargs):
        print("in 'par', param = {}".format(self.param))
        return self.func(*args, **kwargs)


@Foo('sssssss')
def test_class_param_on(a, b):
    return a + b


# @Foo('wsy').par
# def test_class_param_on2(a,b):
#     return a+b

print()
print("test  param class-decorator")
print(test_class_param_on(4, 5))
# print(test_class_param_on2(5,6))
print(Foo('sssssssss')(test_class_param_on)(5, 6))  # 装饰器等价调用
