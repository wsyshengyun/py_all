# -*- coding: utf-8 -*-
'''
@File    :   dict_deaultdict.py
@Time    :   2020/09/23 16:44:06
'''
from collections import defaultdict

# =====================================统计几个key出现过那几个value=======================================
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('red', 1), ('blue', 4)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)

# =====================================统计一个key出现过多少次=======================================
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(d)

# =====================================some=======================================
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)
