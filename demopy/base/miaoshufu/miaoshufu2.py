# coding:utf-8   


class Foo:
    def __init__(self, key, hope_type):
        print("at __init__ of Foo")
        self.key = key
        self.hope_type = hope_type 
    
    def __get__(self, instance, own):
        print("at __get__ of Foo")
        return instance.__dict__.get(self.key, None)

    def __set__(self, instance, value):
        print("at __set__ of Foo")
        if not isinstance(value, self.hope_type):
            raise TypeError("error")
            # raise TypeError(u"你好啊, 这是{}".format(self.hope_type))
        instance.__dict__[self.key] = value 

class Test:
    name = Foo('name', str)
    age = Foo('age', int)
    def __init__(self, name, age, salary):
        print("at __init__ of Test...")
        self.name = name 
        self.age = age 
        self.salary = salary 

f = Test('alex', 18, 2000)
g = Test('wsy', 33, 1000)
print(f.name, g.name)
print(f.age, g.age)
print('=================')
print(f.name)


class Demo:
    x = 10 
    def __init__(self, x=0):
        print("at __init__")
        self.x = x

# obj = Demo() 
# print(obj.x)
