# coding:utf8

"""
    闭   包  的   定   义
如果一个函数内部定义了一个函数, 外部的我们叫他外函数, 内部的我们叫他内函数.
闭包
    在一个外函数中定义了一个内函数,内函数里运用了外函数的临时变量,并且外函数的返回值是内函数
    的引用,这样就构成了一个闭包.
    一般情况下，在我们认知当中，如果一个函数结束，函数的内部所有东西都会释放掉，还给内存，局部变量都会消失。但是闭包是一种特殊情况，如果外函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，就把这个临时变量绑定给了内部函数，然后自己再结束。

"""


def outer(a):
    b = 10

    def inner():
        print(a + b)

    return inner


demo = outer(5)
demo()  # 15

demo2 = outer(7)
demo2()  # 17

def outer(a):
    b = 10
    c = [a]

    def inner():
        nonlocal b
        b += 1

        # 方法2 修改闭包变量
        c[0] += 1
        print(c[0])
        print("c[0] is {}".format(c[0]))
        print("b is {}".format(b))
        print("as is {}".format(a))
    return inner

bbf = outer(5)
bbf()