# coding:utf8

# and 和 or 的短路效应
# 当一个or表达式中所有值都为真时, python会选择第一个值
# 当一个and表达式中所有值都为真时, python会选择最后一个值
print(2 or 3)  # 2
print(5 and 6 and 7)  # 7

# 可省略续航符
my_list = [1, 2, 3,
           4, 5, 6]
list1 = (1, 2, 3,
         4, 5)
set1 = {1, 2, 3, 4,
        5, 6}
dit1 = {'a': 1, 'b': 2,
        'c': 3, 'd': 4}
str1 = "abc, ed" \
       "abc"  # 字符串不可以, 换行的时候自动添加
str2 = """nihao, nihao
n ihao niyhoa """

# 小整数池
# python定义了一个小整数池[-5, 256]这些整数是提前建立好的, 不会被立即回收,;
a = -6
b = -6
print("a is b: {}".format(a is b))  # True
a = 256
b = 256
print("a is b: {}".format(a is b))  # True
a = 257;  b = 257
print("a is b: {}".format(a is b))  # True


# arguments; 和; parameter; 的翻译都是参数，在中文场景下，二者混用基本没有问题，毕竟都叫参数嘛。 但若要严格再进行区分，它们实际上还有各自的叫法 parameter：形参（formal;
# parameter），体现在函数内部，作用域是这个函数体。 argument ：实参（actual; parameter），调用函数实际传递的参数。 举个例子，如下这段代码，"error"; 为; argument，而; msg;
# 为; parameter。


def output_msg(msg):
    print(msg)


output_msg("error")

# try...finally与return


def fun():
    try:
        return 'nihao'  # nihao 最后输出
    finally:
        print('finally')  # 先输出


print(fun())


# 循环中局部变量的泄露
x = 1 
lit = [x for x in range(5)]
print("lit is :{}".format(lit))
print("x is {}".format(x))  # x的值是1 而不是4


