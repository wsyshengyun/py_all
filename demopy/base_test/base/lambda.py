# coding:utf8

'''
什么是lambda？
Lambda是一种不需要名字（即标识符）、由一个单独表达式成的匿名内联函数，表达式会在调用时被求值。

在Python中，创建 lambda 函数的语法为：

lambda [parameters]: expression
也就是说lambda函数包含三个部分：

关键字lamdbda；
参数；
函数体
lambda函数可以包含任意多的参数，但是函数体部分只能包含一个表达式。

此外，lambda函数用一行代码写成，并且被立即调用。

'''

'''
返回的是一个函数体
'''

from functools import reduce

fun = lambda x: print(x)
fun(5)

# 与python内置函数结合使用
# map 函数

# map(function, iterable, ....)
print(list(map(lambda x: x + 2, [1, 2, 3, 4, 5])))

# reduce
result = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(result)

# lambda
nihao = lambda x: x * 2
result = nihao(4)
print(result)

y = 10
fun = lambda x: y + x
result = fun(20)
#     实际应用中,lambda表达式可以在一个类内,x是一个变量, y可以是一个类变量,比如cls
#     y是已知的;
#     lambda表达式,参数必须含有一个位置的变量;
print(result)

# 测试2 : lambda表达式中参数可以带有默认参数
func = lambda x, y=4: x + y
result = func(3)
print(result)
