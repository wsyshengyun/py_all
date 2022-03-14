# coding: utf-8
from functools import wraps
""" 引用ctypes模块 为了通过id得到id所在的对象
以此了些一个函数还存在不存在 """




import ctypes 
def myfunc():
    print("in myfunc")
    _id = id(myfunc)
    print(_id)
    return _id
""" 得到函数myfunc的id， 看下面把myfunc重新包装后，此函数还存在不存在呢 """
id_myfunc = myfunc()

def log(func):
    # @wraps
    def _inner(*args, **kwargs):
        return func(*args, **kwargs)  
    return _inner

myfunc = log(myfunc)
id_log = id(myfunc)
# print(id_log)
print() 
# value = ctypes.cast(id_myfunc, ctypes.py_object).value
value = ctypes.cast(id_myfunc, ctypes.py_object).value
print(type(myfunc))
print(id_myfunc, value())
""" 实事证明，此函数还是存在的，没有被覆盖掉  """
""" 为什么还存在呢？
我想是因为闭包，因为log函数里面有一个闭包_inner引用了函数myfunc """

# tsr = "nihao"
# ids = id(tsr) 
# def gstd():
#     print('gstd is a function')
#     return True
# idf = id(gstd)
# value = ctypes.cast(idf, ctypes.py_object).value
# print()
# print(ids, value())