# coding: utf8

class Student:
    def __init__(self, name):
        self.name = name 

    @property 
    def math(self):
        return self._math


    @math.setter
    def math(self, value):
        if 0<=value<=100:
            self._math = value 
        else:
            raise ValueError("Valid value must be in 0 to 100")

obj = Student('wsy')
obj.math = 199
print(obj.math)
