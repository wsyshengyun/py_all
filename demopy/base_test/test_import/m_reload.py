# coding:utf8


class MyModule:
    def __init__(self):
        self.a = 1
        self.b = 8
        pass

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def __str__(self):
        return f"<MyModule object: a is {self.a}, b is {self.b}>"
