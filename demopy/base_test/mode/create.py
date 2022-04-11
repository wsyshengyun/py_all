# coding:utf8


import copy


class Prototype(object):

    def clone(self):
        """nihao"""
        return copy.deepcopy(self)


class Register(Prototype):

    def __init__(self, names=[]):
        self.names = names


if '__main__' == __name__:

    obj = Register([1, 2, 3, 4])
    obj_one = obj.clone()
    print(obj)
    print(obj_one)
    print(obj_one.__class__)
    print(obj_one.names)
    obj.names.append(6)
    print(obj_one.names)
    pass
