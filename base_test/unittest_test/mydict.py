# -*- coding: utf-8 -*-
'''
@File    :   mydict.py
@Time    :   2021/11/14 12:54:40

'''
from typing import Any

class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Dict object has no attribute '%s'" % key)
        
    def __setattr__(self, key: str, value: Any) -> None:
        self[key] = value