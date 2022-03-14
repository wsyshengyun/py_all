# coding:utf-8 
""" 
创建特殊用法: 
一个里面创建同类型的兄弟
一个对象创建相同值的兄弟 
 """
class Demo:
    def __init__(self, a, b):
        self.a = a 
        self.b = b 

    
    def make(self):
        return type(self)(self.a, self.b)

    def make_self(self):
        return self

    
    def __str__(self):
        # return "obj is {} : a={}, b={}".format(self, self.a, self.b)
        return "obj  : a={}, b={}".format( self.a, self.b)


obj = Demo(1,4) 
print(obj.make())
print(id(obj), id(obj.make()))
print('-' * 20)
print(obj.make_self(), id(obj.make_self()   ))
print(obj is obj.make_self())

    