# -*- coding: utf-8 -*-
'''
@File    :   meta_upper.py
@Time    :   2020/09/13 22:25:06
'''


def upper_attr(class_naem, class_parents, class_attr):
    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value
        else:
            new_attr[name] = value

    return type(class_naem, class_parents, new_attr)


class Foo(object, metaclass=upper_attr):
    # __metaclass__ = upper_attr 
    bar = 'bip'


obj = Foo()
print(hasattr(obj, 'bar'))
print(hasattr(obj, 'BAR'))
print(obj.BAR)
