# coding:utf8

class A(object):
    def __init__(self) -> None:
        super().__init__()
        print("this class is {}".format(self))


class B(object):
    def __init__(self) -> None:
        super().__init__()
        print("this class is {}".format(self))


class C(object):
    def __init__(self) -> None:
        super().__init__()
        print("this class is {}".format(self))


class D(A, B, C):
    def __init__(self) -> None:
        super().__init__()
        print("this class is {}".format(self))
        print(super(A, self).__init__())


# =====================================类的类变量=======================================
class TestAmn(object):
    a = 1
    b = []

    def __init__(self) -> None:
        super().__init__()
        pass

    def out(self):
        print("cls.a : {}".format(TestAmn.a))
        print("cls.a : {}".format(self.a))
        TestAmn.a += 2
        print("更新后的cls.a : {}".format(self.a))


obj = TestAmn()
obj.out()
