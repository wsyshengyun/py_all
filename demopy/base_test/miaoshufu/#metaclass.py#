# coding:utf-8

class Descriptor(object):
    def __init__(self):
        self.label = None 

    
    def __get__(self, instance, owner):
        print('__get__.Label = %s'%self.label) 
        return instance.__dict__.get(self.label, None) 
    
    def __set__(self, instance, value):
        print("__set__")
        instance.__dict__[self.label] = value 


class DescriptorOwner(type):
    def __new__(cls, name, bases, attrs):
        for n, v in attrs.items():
            if isinstance(v, Descriptor):
                v.label = n 
        return super(DescriptorOwner, cls).__new__(cls, name, bases, attrs) 

class Foo(object):
    __metaclass__ = DescriptorOwner 
    x = Descriptor() 

""" 
为什么输出的结果与原来的不一样呢  
self.label 应该输出为  x 才对  
 """

f = Foo() 
# g = Foo() 
f.x = 10 
# g.x = 19 
print('-'*20)
# print(f.x, g.x)
print(f.x)