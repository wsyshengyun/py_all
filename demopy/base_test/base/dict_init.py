# -*- coding: utf-8 -*-


# 创建空字典
d1 = dict()
d3 = dict(a=1, b=2, c='c')
d1_1 = {}  # 速度比dict()快
d2 = {'a': 1, 'b': 2}
# 生成式方式
lit = [1, 2, 3, 4, 5]
d4 = {str(i): i for i in lit}
# 直接通过可迭代对象生成字典
lit = [('name', 'jonah'), ('age', 14)]
d5 = dict(lit)
# fromkeys方式
# 1, 有一个参数, , 这个参数为字典的键, 参数为一个可迭代对象, key的值为None
# 2, 有两个参数, 第一个参数为一个可迭代对象, 第二个参数为默认的值
d6_1 = dict.fromkeys(['a', 'b', 'c'])  # {'a': None, 'b': None, 'c': None}
d6 = dict.fromkeys(['a', 'b', 'c'], 5)  # {'a': 5, 'b': 5, 'c': 5}
g1 = (i for i in [1, 2, 3])  # 生成器
d62 = dict.fromkeys(g1)  # {1: None, 2: None, 3: None}

# dict + key
d_ = {'a': 1, 'b': 2}
d7 = dict(d_, c=3)

# zip 方式
d8 = dict(zip(['a', 'b', 'c'], [1, 2, 3, ]))

# map 方式
mp = map(lambda x, y: (x, y), 'ABCD', range(1, 5))
d8_1 = dict(mp)

# copy 方式
d9 = d_.copy()
assert d9 == {'a': 1, 'b': 2}

# 修改字典的key或者value
dit = {'a': 1, 'b': 2, 'c': 3}
# result = dit.setdefault('d', default=8)   报错, default去掉
result1 = dit.setdefault('d', 8)
result2 = dit.setdefault('c', 33)
assert dit == {'a': 1, 'b': 2, 'c': 3, 'd': 8}
assert result1 == 8
assert result2 == 3

# update
# 字典参数
dx = {'a': 1, 'b': 2, 'c': 3}
db = {'d': 4, 'e': 5}
dx.update(db)
assert dx == {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 关键字参数
dx.update(f=6)
assert dx.get('f') == 6

# update 混合参数  dict与关键字参数 kwargs
dx = {'a': 1, 'b': 2, 'c': 3}
db = {'d': 4, 'e': 5}
dx.update(db, f=6, g=7)
assert dx.get('d') == 4
assert dx.get('g') == 7

# 字典的用途
temp = '姓名:%(name)s,年龄:%(age)3.0f,籍贯:%(location)s'
msg = {'name': 'JoJ', 'age': 23, 'location': '海拉尔群岛'}
print(temp % msg)
# 字典可以排序,在python3.6之后,但是之前不可以排序
dict_1 = {str(i): i for i in range(5)}
print(dict_1)
# 在运行效率上，{} 会比 dict() 快三倍左右