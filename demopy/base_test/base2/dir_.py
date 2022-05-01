# coding:utf8


class A:
    aa = 4

    def __init__(self, a=2):
        """ """
        self.a = a

    def __contains__(self, item):
        print('__contains__')

    @staticmethod
    def foo():
        print("foo")


def func(a):
    print("in func")
    print(a)


def test():
    dit = {}
    a = 2
    lit = []
    obj = A()
    # V1 有  'aa'
    # v2 有'a' 和 'aa'
    v1 = dir(A)
    v2 = dir(obj)
    v3 = dir(dit)
    v4 = dir(a)
    v5 = dir(lit)
    v6 = dir()
    pass
    print(
        v1, '\n', '-'*50, '\n',
        v2, '\n', '-'*50, '\n',
        v3, '\n', '-'*50, '\n',
        v4, '\n', '-'*50, '\n',
        v5, '\n', '-'*50, '\n',
        v6, '\n', '-'*50, '\n',
            )


# test()


def test_module_upper_name():
    from demopy.base_test.base2 import default_settings
    print('-' * 30)
    for name in dir(default_settings):
        # 摒弃掉了__开头的name对象
        if name.isupper():
            print(name, '==>', getattr(default_settings, name))


test_module_upper_name()

