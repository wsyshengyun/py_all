# coding:utf8

'''

如果父类的函数被继承,父类函数的return 将会被忽略.
子类函数运行到此,super(子类名, self).foo() ,并不会返回退出.
可以继续运行下面的语句.
'''

class A(object):

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = None
        pass


    def foo(self):

        print('I is foo')
        self.c = self.a + self.b
        return self.c



class Achild(A):

    def __init__(self):
        super(Achild, self).__init__()


    def foo(self):
        super(Achild, self).foo()
        self.c += 1
        print(self.c)


def main():
    obj = Achild()
    obj.foo()
    pass


main()

