# coding:utf8


class Attr:
    b = 11
    print('pos is at class....')

    def __new__(cls, *args, **kwargs):
        print("__new__")
        print(f"cls.b is init = {cls.b}")
        # cls.b = 0
        # obj = super().__new__(cls)
        obj = object.__new__(cls)
        obj2 = object.__new__(cls)

        print(f"obj1.b is {obj.b}")
        print(f"obj2.b is {obj2.b}")
        print(f"id(obj) is {id(obj)}")
        print(f"id(obj2) is {id(obj2)}")

        print(f'self is obj, id(obj) is {id(obj)}')
        return obj

    def __init__(self, master=None):
        print('__init__')
        # self.b = 10
        self.master = master
        print(f"id(self) is {id(self )}")

    def __str__(self):
        return f"master is {self.master}, b is {self.b}"

    def __call__(self, *args, **kwargs):
        return 5
        pass


def get_class():
    print('------get_class------------')
    ClassVar = type('ClassA', (object, ), dict(name="type test"))
    a = ClassVar()
    print(type(a))
    print(a.name)
    print('---------end-------')


if __name__ == '__main__':
    obj = Attr(5)
    print(obj)
    print('obj is callable? ', end='')
    print(callable(obj))
    print(f"obj() is {obj()}")
    print(f"obj type is {type(obj) }")
    print(f"obj type is {obj.__class__}")
    get_class()

