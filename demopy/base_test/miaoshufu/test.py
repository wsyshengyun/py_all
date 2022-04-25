# coding:utf-8


class Demo:
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __repr__(self):
        print("..repr..")
        pass

    # def __str__(self):
    #     return "str...."


obj = Demo()
print(obj)
