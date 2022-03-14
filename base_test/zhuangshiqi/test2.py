# codeing:utf8

'''
装饰器  
    )))本质上是一个函数
    )))增加其它函数的功能而不修改其代码
    )))为已经存在的或对象 添加额外的功能  
    )))返回值   也是一个函数对象  
    )))参数呢?? 
'''


def debug(func):
    def wrapper(something):
        pass
        return func(something)
    return wrapper 

@debug
def say_hello():
    print("hello")


say_helloi()

