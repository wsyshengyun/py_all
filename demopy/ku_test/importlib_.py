# coding:utf8

from importlib import import_module


module = import_module('_test')
# module2 = import_module('base_test.base.base')   报错; 找不到模块
module2 = import_module('demopy.base_test.base.base')
print('-'*60)
module.foo()
print(module2.x)