# -*- coding: utf-8 -*-
'''
@File    :   single.py
@Time    :   2020/09/14 08:55:57
'''
""" 定义单列类；这个类其实是元类；因为继承了type """

class Singleton(type):

    def __call__(self, *args, **kwargs):
        if not hasattr(self, '_instance'):
            self._instance = super().__call__(*args, **kwargs)
        return self._instance

""" Foo类使用了singleton进行创建 """
class Foo(object, metaclass=Singleton):
    pass


f1 = Foo()
f2 = Foo()
print(f1)
print(f2)
print(f1 is f2)
print(f1 is f2) 
