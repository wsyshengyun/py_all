# -*- coding: utf-8 -*-
'''
@File    :   look_os.py
@Time    :   2020/09/22 17:41:29
'''

import os
import types

# os_list_str = dir(sys) 
os_list_str = dir(os)
_module = os


def print_val(tsr):
    global _module
    val = getattr(_module, tsr)
    print(tsr, ': ', repr(val))


paichu_types = [types.FunctionType, types.BuiltinFunctionType, type]
for tsr_ele in os_list_str:
    if tsr_ele == 'environ' or \
            tsr_ele[0].isupper() == True or \
            tsr_ele.startswith('_'):
        continue
    result = getattr(_module, tsr_ele)
    if type(result) not in paichu_types:
        # print(tsr_ele)
        print_val(tsr_ele)
