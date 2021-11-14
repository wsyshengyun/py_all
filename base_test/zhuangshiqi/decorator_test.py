# codeing:utf8
import functools
from typing import Any
import functools

'''
 
'''
#=====================================普通装饰器=======================================
def pt(func):
    @functools.wraps(func)
    def __inner(*args, **kwargs):
        print('on before')
        func(*args, **kwargs)
        print('on after')
    return __inner
@pt
def foo():
    print('I is foo function')

foo()

#=====================================带参数的装饰器=======================================
def ptp(level):
    def _inner(func):
        @functools.wraps(func)
        def _bottom(*args, **kwargs):
            print("{}: enter {}()".format(level, func.__name__))
            func(*args, **kwargs)
        return _bottom
    return _inner
@ptp(level='INFO')
def poo():
    print("I'm is poo")

poo()

#=====================================类装饰器=======================================
# 不带参数的装饰品
# 类的成员为函数名， __call__函数的参数为被装饰的函数的参数 *args, **kwargs 
# 被装饰的函数变成了类对象了？？？ 
class A:
    def __init__(self, func) -> None:
        self.func = func
        pass
        
    def __call__(self,*args, **kwargs):
        print("is class decorator start")
        self.func(*args, **kwargs)

@A
def fun():
    print("nihao")

print("func=========")
fun()
print("fun的type是： {}".format(type(fun)))
print("")
#=====================================类装饰器带参数=======================================
class At:
    def __init__(self, level) -> None:
        self.level = level
        pass 

    
    def __call__(self, func, *args: Any, **kwds: Any) -> Any:
        @functools.wraps(func)
        def _inner(*args, **kwargs):
            print("{0}: enter {1}".format(self.level, func.__name__))
            func(*args, **kwargs)
        return _inner

@At('INFO')
def foo_c():
    print('is foo_c')

foo_c()
print("function name is : {}".format(foo_c.__name__))
        
        