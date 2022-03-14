# -*- coding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/12/01 21:36:07
'''

class FunctionList:
    def __init__(self, value=None) -> None:
        if value is None:
            self.values=[] 
        else:
            self.values = value 

    def __len__(self):
        return len(self.values)
    
    def __getitem__(self, key):
        return self.values[key]
    
    def __setitem__(self, key, value):
        self.values[key] = value
    
    def __del
