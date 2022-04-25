# -*- coding: utf-8 -*-
'''
@File    :   mofa.py
@Time    :   2021/09/20 21:48:46
python一些魔法函数的问题
'''
import sys

# def Log(msg):
# print("Line: {} -- ".format( sys._getframe().f_lineno), msg)
fl = sys._getframe


class Test(object):
    def __init__(self, data=1):
        self.data = data
        self.a = 12

    def __iter__(self):
        return self

    def __next__(self):
        if self.data > 9:
            raise StopIteration
        else:
            self.data += 1
            return self.data


for item in Test(2):
    print('[%s] - ' % (sys._getframe().f_lineno), item)


# -----------------------------------------------------------
# __lt__ : less than 
# -----------------------------------------------------------

class People(object):
    def __init__(self, name, age):
        print(fl().f_lineno, "__init__ is call ")
        self.name = name
        self.age = age
        self.a = [1, 2, 3, 4, 5]

    def __str__(self) -> str:
        return self.name + " ：" + str(self.age)

    def __lt__(self, other):
        return self.name < other.name if self.name != other.name else self.age < other.age

        # def __str__(self) -> str:

    #     return "this is string %s" % (len(self.a) + 100)

    def __repr__(self) -> str:
        return str(len(self.a) + 100)

    def __setattr__(self, name, value) -> None:
        print(fl().f_lineno, "__setattr__ is call, name is : %s value is : %s" % (name, value))
        return super().__setattr__(name, value)

    def __getattr__(self, name):
        print(fl().f_lineno, "__getattr__ is call, name is: %s" % name)
        # return super().__getattr__(name)
        pass

    def __getattribute__(self, name: str):
        print(fl().f_lineno, "__getattribute__ is call")
        return super().__getattribute__(name)

    def __delattr__(self, name):
        print('[%s] - ' % (sys._getframe().f_lineno), "__delattr__ () is called...")

    def __setitem__(self, name, value):
        """ obj[bjm] """
        print('[%s] - ' % (sys._getframe().f_lineno), "__setitem__ is called...")
        pass

    def __getitem__(self, name):
        print('[%s] - ' % (sys._getframe().f_lineno), "__getitem__ is called ")
        pass

    def __iter__(self):
        return iter(self.a)
        pass

    def __del__(self):
        print('[%s] - ' % (sys._getframe().f_lineno), "__del__ is called... ")
        pass


def main_people():
    # print(fl().f_lineno,"\t".join([str(item) for item in sorted([
    #     People("abc", 19), 
    #     People("abc", 12 ),
    #     People("abc", 17),
    #     People("abc", 21),
    #     People("edf", 21),
    #     People("xyz", 21),
    # ])]))
    # print(fl().f_lineno, "in f - main_people()")
    # print(fl().f_lineno, People('wsy', 35))
    # print(fl().f_lineno, "%r" % People('wsy', 35))
    # print(fl().f_lineno, repr(People('wsy', 35)))
    obj = People('wsy', 35)
    # del obj.name

    # obj['bjm']
    # obj['bjm'] = 12

    # _dit = {}
    # b = 12
    # c = 'xy'
    # _dit['a'] = 5 
    # _dit[b] = 6 
    # _dit[c] = 100
    # print('[%s] - '% (sys._getframe().f_lineno),_dit)

    # for i in obj:
    # print('[%s] - '% (sys._getframe().f_lineno), i )

    del obj.name
    pass


main_people()


# ============================================================================
def main():
    obj = Test()
    obj = 0
    pass
