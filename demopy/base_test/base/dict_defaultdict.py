# coding:utf8

from collections import defaultdict


list1 = [1, 2, 1, 3, 1]
# dict1 = defaultdict(list)
dict1 = defaultdict(int)
for k in list1:
    dict1[k] += 1

print(dict1)
print(dict(dict1))

dict_l = defaultdict(list)
dict_l[1].append('a')
dict_l[1].append('b')
# dict_l[2] = 'j'
print(dict(dict_l))

# 2
dict2 = {}
for k in list1:
    if k in dict2:
        dict2[k] += 1
    else:
        dict2[k] = 1
print(dict2)


# 3
dict3 = {}
for k in list1:
    dict3.setdefault(k, 0)
    dict3[k] += 1
print(dict3)
