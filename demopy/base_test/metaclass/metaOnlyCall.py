# -*- coding: utf-8 -*-
'''
@File    :   metaOnlyCall.py
@Time    :   2020/09/14 06:46:39
'''


class MyMeta(type):
    def __call__(self, *args, **kwargs):
        if args:
            raise TypeError("must be keyword argument")
        obj = self.__new__(self, *args, **kwargs)
        for key, value in kwargs.items():
            setattr(obj, key.upper(), value)
        return obj
        # return super().__call__(*args, **kwargs)


class Student(object, metaclass=MyMeta):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def tell(self):
        print("%s的信息是：%s" % (self.NAME, self.AGE))


student = Student(name='wsy', age=25)
student.tell()

'''
在元类中控制自定义的类无需__init__方法
1.元类帮其完成创建对象，以及初始化操作
2.要求实例化时传参必须为关键字形式，否则抛出异常TypeError: must use keyword argument
3.key作为用户自定义类产生对象的属性，且所有属性变成大写
'''

# class MyMeta(type):
#     def __call__(cls, *args, **kwargs):
#         if args:
#             raise  TypeError('must use keyword argument')
#         obj = cls.__new__(cls,*args,**kwargs)
#         for key,value in kwargs.items():
#             setattr(obj,key.upper(),value)
#             #obj.__dict__[key.upper()]=v
#         return obj


# class Student(object,metaclass=MyMeta):
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls)

#     def tell(self):
#         print(u"%s 的信息是:%s"%(self.NAME,self.AGE))

student = Student(name='wtt', age=25)
student.tell()
