# coding:utf8

"""
*loc 作为参数的时候, 在函数体内loc就是(loc, ), 变成了一个元组, *loc就是对元组进行解包,编程loc本身;
    在函数内部 *loc才是其本身
loc作为参数的时候, 在函数内部loc还是loc, *loc是对其解包,编程一个个元素
    在函数内部 *loc是对loc进行解包

"""

''
def foo(*loc):
    print('---in foo---')
    print("loc is : {}".format(loc))
    print("*loc is {}".format(*loc))


def fun(loc):
    print('---in fun---')
    print("loc is : {}".format(loc))
    print("*loc is {}".format(*loc))


if __name__ == '__main__':
    print("loc为一个列表, 有三个元素")
    list_loc = [1,2,3]
    foo(list_loc)
    fun(list_loc)

    print("loc为一个元组,只有一个元素")
    list_loc = (1,)
    foo(list_loc)
    fun(list_loc)

    print('loc 为 一个整数')
    foo(2)

