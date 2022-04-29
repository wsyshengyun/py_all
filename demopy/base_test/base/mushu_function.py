# coding:utf8
"""


"""


class Test(object):
    c = 0  # 不会调用__setattr__

    def __init__(self, a=0):
        print("__init__")
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
        return self.__dict__[item]
        pass

    def __set__(self, instance, value):
        """ 描述符相关"""
        print('__set__')
        pass

    def __get__(self, instance, owner):
        """ 描述符相关"""
        print('__get__')
        pass

    def __getitem__(self, item):
        # test['a'] 时被调用
        print('__getitem__')
        pass

    def __setitem__(self, key, value):
        print('__setitiiem__')
        pass

    def __call__(self, *args, **kwargs):
        print('__call__')
        pass

    def __iter__(self):
        print('__iter__')
        pass

    def __next__(self):
        print('__next__')
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
