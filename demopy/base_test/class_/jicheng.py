# coding:utf8

class A(object):
    def __init__(self, a):
        """ """
        self.a = a

    def foo(self):
        print("obj a is {}".format(self.a))


class B(A):
    def __init__(self, a):
        """ """
        super(B, self).__init__(a)  # 这个参数还是需要传递的,不然报错



if __name__ == '__main__':
    objb = B(2)
    objb.foo()