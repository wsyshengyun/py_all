# coding:utf8
"""
单例模式
"""


class MySinglection:
    __obj = None  # 类属性, 标志创建对象是否存在,如果存在则返回
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if None == cls.__obj:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, name):
        if MySinglection.__init_flag:
            print("Init...")
            self.name = name
            MySinglection.__init_flag = False
