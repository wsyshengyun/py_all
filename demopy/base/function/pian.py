# coding:utf8  

'''
'''
from functools import partial 
import functools
def sum(*args):
    s = 0 
    for n in args:
        s+=n 
    return s 

sum_add_10 = partial(sum, 10) 
sum_add_10_20 = partial(sum, 10, 20) 
print(sum_add_10(1,2,3,4,5))
print(sum_add_10_20(1,2,3,4,5))



sum_add_chu = partial(sum, 1,2,3,4,5)
print(sum_add_chu(10))
print(sum_add_chu(10, 20))

sum_other = functools.partial(sum, 20) 
print(sum_other(20))