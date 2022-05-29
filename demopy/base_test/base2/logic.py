# coding:utf8

"""
for 循环, 如果遇到break, 就不会执行else后面的语句了
while 循环也一样;
"""


# for ... else ...
def foo(a):
    for i in range(8):
        if i > a:
            print("break , a is :{}".format(a))
            break
    else:
        print('else....')


foo(9)


def test_while(a):
    i = 0
    while i > a:
        print(i)
        i += 1
        # if i > a:
        #     print('break...')
        #     break
    else:
        print('else....')


test_while(10)
