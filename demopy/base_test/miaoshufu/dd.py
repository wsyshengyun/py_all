# coding: utf-8


class Score:
    def __init__(self, c=0):
        print("__init__")
        self.c = c

    def __get__(self, instance, owner):
        print("__get__")
        return self.c

    def __set__(self, instance, value):
        print("__set__")
        if not isinstance(value, int):
            raise TypeError("Score must be integer")
        if not 0 < value <= 100:
            raise ValueError("Valid value must be in 0 to 100")
        else:
            self.c = value


class Person:
    enlish = Score()
    math = Score()
    dili = Score()

    def __init__(self, name, math, dili, enlish):
        super().__init__()
        self.name = name
        self.math = math
        self.dili = dili
        self.enlish = enlish

    def __repr__(self):
        return "<Student:{}, math:{}, dili:{}, english:{}>".format(self.name
                                                                   , self.math, self.dili, self.enlish)

    def __str__(self):
        return super().__str__()


obj = Person('wsy', 10, 20, 90)
objsome = Person('lrf', 33, 50, 98)
print(obj)
print(objsome)
