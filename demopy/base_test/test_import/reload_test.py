# coding:utf8

# import imp python 3.0 到3.3可以使用imp模块
# python3.3以上就要使用importlib模块了
import importlib
import sys

sys.path.append('d:\_python\pythonG')
from demopy.base_test.test_import.m_reload import MyModule
import m_reload

"""
使用reload的时候,一定要用import 不能用from...import...导入一个模块
reload函数接受的是一个模块对象,而不是别的对象
"""

obj = MyModule()
print(obj)


def reload():
    """测试通过"""
    importlib.reload(m_reload)
    # obj = MyModule()
    obj = m_reload.MyModule()
    print(obj)


def reload_from_sys():
    """测试通过
    from foo import bar 这种方式，想使用移除 sys.modules 来重载模块这种方法是失效的"""
    import sys
    if sys.modules['m_reload']:
        del sys.modules['m_reload']
    import m_reload
    obj = m_reload.MyModule()
    print(obj)

def reload_5():
    """ !!!测试不通过"""
    m_reload.__spec__.load_module()
    obj = m_reload.MyModule()
    print(obj)

