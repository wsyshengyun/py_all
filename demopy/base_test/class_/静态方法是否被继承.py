# coding:utf8

# TODO 结果呢?是否会自动继承父类的静态方法呢?
class A:
    @staticmethod
    def foo_static():
        """ """
        print('static, in A')

    @classmethod
    def fun_clsmethod(cls):
        print('classmethod, in B')


class B(A):
    @staticmethod
    def foo_static():
        """ """
        print('static, in B')

    @classmethod
    def fun_clsmethod(cls):
        print('classmethod, in B')


if __name__ == '__main__':
    obja = A()
    objb = B()
    # 输出结果
    # static, in A
    # classmethod, in B
    # static, in B
    # classmethod, in B
    #
    # 所以如果子类的类方法与父类的类方法同名, 将覆盖父类的类方法
    #

    obja.foo_static()
    obja.fun_clsmethod()
    objb.foo_static()
    objb.fun_clsmethod()
    print('-'*60)
    # 输出结果  同上面一样
    # static, in A
    # classmethod, in B
    # static, in B
    # classmethod, in B)
    A.foo_static()
    A.fun_clsmethod()
    B.foo_static()
    B.fun_clsmethod()

