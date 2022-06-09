# coding:utf8

from copy import copy, deepcopy


# copy是否可以深copy，从copy数组上来测试
# 体会变与不变
a = [1, 2, 3]
b = a.copy()
print(a, b)
print(id(a), id(b))
a.append(4)  # 结果不一样， 原列表增加一个元素， 复制列表b不变
print(a, b)
a[0] = 11  # 原列表的一个位置元素改变，复制列表不变
print(a, b)

a = [1, 2, [3, 4, 5], 6]
b = a.copy()
c = deepcopy(a)
print(a, b, c)
print(id(a), id(b), id(c))
a[2].append(66)  # 如果原列表里面有一个可变的对象，那么这个可变对象变化的时候，copy的列表也根着变化，但是deepcopy不变
print(a, b, c)



