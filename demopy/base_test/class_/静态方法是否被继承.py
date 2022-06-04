# coding:utf8


"""
总结：
静态方法可以被子类继承，如果子类有同名的静态函数，则会覆盖父类的静态方法，即是参数不一样只在方法名字一样就会覆盖；
类方法和静态方法是一样的；
"""
class A:
    @staticmethod
    def foo_static1():
        print('static method in A, name is > foo_static1')

    @staticmethod
    def foo_static2():
        print('static method in A, name is > foo_static1')

    @staticmethod
    def foo_static():
        """ """
        print('static method in A, name is > foo_static')

    @classmethod
    def func_clsmethod(cls):
        print('classmethod, in A, name is > func_clsmethod')

    @classmethod
    def func_clsmethod1(cls):
        print('classmethod, in A, name is > func_clsmethod1')


class B(A):
    @staticmethod
    def foo_static():
        """ """
        print('static method in B, name is > foo_static')

    @staticmethod
    def foo_static2(a):
        print('static method in B, name is > foo_static1, 参数是{}'.format(a))

    @classmethod
    def func_clsmethod(cls):
        print('classmethod, in B, name is > func_clsmethod')


if __name__ == '__main__':
    obja = A()
    objb = B()
    objb.foo_static()
    objb.foo_static1()
    objb.foo_static2(6)
    objb.func_clsmethod()
    objb.func_clsmethod1()



