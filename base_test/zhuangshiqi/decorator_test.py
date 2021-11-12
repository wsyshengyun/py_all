# codeing:utf8

'''
 
'''


def debug(func):
    def wrapper(something):
        pass
        return func(something)
    return wrapper 

@debug
def say_hello():
    print("hello")


