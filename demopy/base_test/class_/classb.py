# coding:utf8 


# -----------------------------------------------------------
# 测试super 
# -----------------------------------------------------------
class A(object):
    def __init__(self, a):
        self.a = a
        print("this class is : {}".format('A'))
        print("canshu is {}".format(self.a))
        pass

    def printOf(self):
        print("nihao")


class B(A):
    def __init__(self, a):
        print("this class is : {}".format(self))
        # super(B, self).__init__()
        # super().__init__()
        # super().__init__(5)


# -----------------------------------------------------------
# 类的学习
# -----------------------------------------------------------
class Study(object):
    ca = 0
    cb = 1
    cc = []

    def __init__(self, a, b=2) -> None:
        super().__init__()
        self.a = a
        self.b = b

    def out(self):
        print("两个参数的值为{}和{}".format(self.a, self.b))

    @classmethod
    def out_cls(cls):
        # print("对象的全局成员有{}、{}和{}".format(cls.ca, self.cb, cls.cc))
        print("类的全局成员有{}、{}和{}".format(cls.ca, cls.cb, cls.cc))

    def out_self_cls(self):
        print("对象的全局成员有{}、{}和{}".format(self.ca, self.cb, self.cc))


def main_study():
    obj = Study(12)
    obj.out()

    obj.ca = 10
    obj.cb = 20
    obj.cc.append(30)
    obj.out_cls()
    obj.out_self_cls()
    pass


if __name__ == "__main__":
    main_study()
