# coding:utf8  

from types import FunctionType, MethodType  
class Foo(object):
    def __init__(self):
        self.name = "wsy"
        self.class1 = "senior"

    def func(self):
        print('123')
        # print(self.name, self.class1)  


obj = Foo()  
#print(obj)
#print(type(obj.func))
#print(isinstance(obj.func, MethodType))
#print(type(Foo.func))
#print(isinstance(Foo.func, FunctionType))
print(obj.func()) 
print('-----')
print(Foo.func(123))
