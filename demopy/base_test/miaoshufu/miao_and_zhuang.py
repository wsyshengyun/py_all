# coding:utf-8

""" classmethod的重实现 """
class NewDefine_classmethod:
    def __init__(self, func):
        print("__init__")
        self.func = func 
    
    def __get__(self, instance, owner):
        print("instance :{}, owner: {}".format(instance, owner))
        print("enter __get__")
        def wrapper(*args, **kw):
            print("enter wrapper function")
            self.func(owner, *args, **kw)
            print('__get__ args is {}'.format(args))
            pass
        return wrapper

# 方式2表示
def study_1(cls, a, b):
    '''
    与下面的study_1对应 
    '''
    print("I am study function, my name is {},  args is {} and {}".format(cls.name, a, b))
    

class Person:
    name = 'wsy'
    # 方式2表示
    study = NewDefine_classmethod(study_1)
    def __init__(self):
        pass

    # 方式1表示
    @NewDefine_classmethod
    def study_2(cls):
        pass




print(Person.study(1,2))
print('----------------------------------------')
print(Person.__dict__['study'].__get__(None, Person)(1,2))
print('----------------------------------------')
