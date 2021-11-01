# coding:utf-8  


class Property:
    def __init__(self, var_name, var_type, var_default_value=None):
        self.var_name = var_name
        self.var_type = var_type
        self.var_default_value = var_default_value if var_default_value is not None else var_type()
        pass

    def __get__(self, instance, owner):
        if self.var_default_value is None:
            return self.var_type()
        else:
            return instance.__dict__.get(self.var_name, self.var_default_value)


    def __set__(self, instance, value):
        if type(value) is not self.var_type:
            raise TypeError("value type is valid")
        instance.__dict__[self.var_name] = value


    def __delete__(self, instance):
        raise AttributeError("不能删除的属性")

class Student(object):
    name = Property('name', str, "Wsy")
    age = Property('age', int) 

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '[name: {}, age: {}]'.format(self.name, self.age)


stu = Student('wsy', 33) 
stu2 = Student('lrf', 30) 
print(stu)
print(stu2)
