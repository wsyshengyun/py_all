# coding:utf8
"""


"""


class Test(object):
    c = 0  # 不会调用__setattr__

    def __init__(self, a=0):
        self.a = a  # 会调用__setattr__
        self.b = 6  # 会调用__setattr__
        self.L = []  # 会调用__setattr__

    # def __getattribute__(self, item):
    #     print("__getattribute__")
    #     pass

    def __setattr__(self, key, value):
        """
        :key is 'b'  字符串类型
        :value is 要给 'b' 设置的值
        """
        print("__setattr__")
        pass

    def __getattr__(self, item):
        """
        只有当__getattribute__不存在时,才会调用
        item: 被访问的变量的字符串;  比如 'a'
        """
        print("__getattr__")
        pass

    def __set__(self, instance, value):
        """ 描述符相关"""
        pass

    def __get__(self, instance, owner):
        """ 描述符相关"""
        pass

    def __getitem__(self, item):
        # test['a'] 时被调用
        pass

    def __setitem__(self, key, value):
        pass

    def __call__(self, *args, **kwargs):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


test = Test(11)
# test.a
# Test.c
# test.d
# test.a = 1
# Test.c = 2
# test.e = 10
# test['a'] = 10
test['b']
