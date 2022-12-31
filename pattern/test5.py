# coding:utf8
from abc import ABCMeta

""" 
结论: 
继承自ABCMeta的类 可以写抽象方法;
而他们的子类可以不完全继承它的抽象方法, 可以只实现其中一部分;  

"""

class Iso(metaclass=ABCMeta):
    def get_name(self):
        pass

    def gettype(self):
        pass


class AIso(Iso):
    def get_name(self):
        return 'nihao'

    def gettype(self):
        return 'Mytype'


class BIso(Iso):

    def __init__(self):
        pass

    def get_name(self):
        return 'bjm'


if __name__ == '__main__':
    bobj = BIso()
    print(bobj.get_name())

    aobj = AIso()
    print(aobj.get_name())

    obj = Iso()
    print(obj.get_name())
    print('='*20)
    print(round(1))
    import os.path
    path = "d://_python//my//pythonG//log//log.log"
    path = r"d:\c\b.txt"
    print(os.path.splitext(path))
