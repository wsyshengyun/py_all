# -*- coding: utf-8 -*-
'''
@File    :   meta_upper_class.py
@Time    :   2020/09/13 22:39:40
'''

""" 把一个类的非__开关的属性全部改为大写 """


class UpperAttrMetaClass(type):
    """ 通过改变..new..来改变metaclass类 """

    def __new__(cls, class_name, class_parents, class_attr):
        new_attr = {}
        for name, value in class_attr.items():
            if not name.startswith("__"):
                new_attr[name.upper()] = value
            else:
                new_attr[name] = value
        return type(class_name, class_parents, new_attr)


class UpperAttrMetaClass2(type):
    """ 通过改变__init__来创建metaclass类 """

    def __init__(self, object_or_name, bases, cls_dict):
        for name, value in cls_dict.items():
            if not name.startswith("__"):
                name_new = name.upper()
                delattr(self, name)
                setattr(self, name_new, value)
        super().__init__(object_or_name, bases, cls_dict)


class Foo(object, metaclass=UpperAttrMetaClass2):
    # __metaclass__ = upper_attr 
    bar = 'bip'


obj = Foo()
print(hasattr(obj, 'bar'))
print(hasattr(obj, 'BAR'))
print(obj.BAR)
