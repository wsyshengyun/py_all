# -*- coding: utf-8 -*-
'''
@File    :   iftypes.py
@Time    :   2020/09/27 22:36:45
'''

import types


class Iftest(object):
    def __init__(self, module):
        self.module = module
        self.ele_tsr_list = dir(self.module)
        self.types_func = types.FunctionType
        self.types_build_func = types.BuiltinFunctionType
        self.types_build_method = types.BuiltinMethodType
        self.types_class = type

    def is_types(self, tsr, typeName):
        if type(getattr(self.module, tsr)) == typeName:
            return True
        else:
            return None

    def out(self):
        for ele_tsr in self.ele_tsr_list:
            if self.is_types(ele_tsr, self.types_func):
                print("func: ", ele_tsr)
            elif self.is_types(ele_tsr, self.types_class):
                print("class: ", ele_tsr)
            elif self.is_types(ele_tsr, self.types_build_func):
                print("build_func: ", ele_tsr)
            elif self.is_types(ele_tsr, self.types_build_method):
                print("build_method: ", ele_tsr)


def main():
    import multiprocessing
    obj = Iftest(multiprocessing)
    obj.out()


if __name__ == '__main__':
    main()
