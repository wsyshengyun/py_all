# coding:utf8  

import functools
from functools import partial

"""
偏函数?
高阶函数
"""


def sum_a(*args):
    s = 0
    for n in args:
        s += n
    return s


sum_add_10 = partial(sum_a, 10)
sum_add_10_20 = partial(sum_a, 10, 20)
print(sum_add_10(1, 2, 3, 4, 5))
print(sum_add_10_20(1, 2, 3, 4, 5))

sum_add_chu = partial(sum_a, 1, 2, 3, 4, 5)
print(sum_add_chu(10))
print(sum_add_chu(10, 20))

sum_other = functools.partial(sum_a, 20)
print(sum_other(20))

# 高阶函数
from functools import reduce
from operator import add

value = reduce(add, range(100))
print(value)  # 4950
