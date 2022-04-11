# coding:utf8

class Miao(object):

    def __init__(self, name):
        self.name = name
        pass

    def __set__(self, instance, value):
        # instance.__dict__[self.name] = value
        pass


class Manage(object):
    a = Miao('a')

    def __init__(self):
        # self.a = 1
        pass


# obj = Manage()
# print(obj.a)
# obj.a = 2
# print(obj.a)


# try:
#     a = 5 / 0
# except ValueError:
#     print('nihao')
# finally:
#     print("finally")

"""
上下文管理器
"""


class TestContext:
    def __enter__(self):
        print("__enter__")
        return 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exc_type is {}'.format(exc_type))
        print("exc_val is {}".format(exc_val))
        print("exc_tb is {}".format(exc_tb))


#
# with TestContext() as t:
#     # a = 1/0
#     print("t is {}".format(t))

# from contextlib import contextmanager
#
#
# @contextmanager
# def test():
#     print("before")
#     yield "hello"
#     print("end")
#
#
# with test() as t:
#     print(t)
#     print(t == 'hello')
#     print('nihao')

from contextlib import closing


class test:
    print('test init')

    def close(self):
        print("self is : {}".format(self))
        print("closed")


with closing(test()) as p:
    print("p is {}".format(p))
    print("doing something")
