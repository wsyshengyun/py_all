# -*- coding: utf-8 -*-


# 创建空字典
d1 = dict()
d3 = dict(a=1, b=2, c='c')
d4 = dict(d3, e=3) # dict + key
d5 = dict((('name', 'jonah'), ('age', 14)))
d5_ = dict(zip(['a', 'b', 'c'], [1, 2, 3, ])) # zip 方式
d6 = d5_.copy()  # copy 方式
d7 = dict(map(lambda x, y: (x, y), 'ABCD', range(1, 5)))  # map方式


d11 = {}  # 速度比dict()快
d12 = {'a': 1, 'b': 2}
# 生成式方式
d13 = {str(i): i for i in range(1, 5)}  # 1, 4  左闭右开

# fromkeys方式, 直接通过可迭代对象生成字典
# 1, 有一个参数, , 这个参数为字典的键, 参数为一个可迭代对象, key的值为None
d14 = dict.fromkeys(['a', 'b', 'c'])  # {'a': None, 'b': None, 'c': None}
d16 = dict.fromkeys((i for i in [1, 2, 3]))  # {1: None, 2: None, 3: None}
# 2, 有两个参数, 第一个参数为一个可迭代对象, 第二个参数为默认的值
d15 = dict.fromkeys(['a', 'b', 'c'], 5)  # {'a': 5, 'b': 5, 'c': 5}


# 修改字典的key或者value
dit = {'a': 1, 'b': 2, 'c': 3}
# result = dit.setdefault('d', default=8)   报错, default去掉
result1 = dit.setdefault('d', 8)
result2 = dit.setdefault('c', 33)
assert dit == {'a': 1, 'b': 2, 'c': 3, 'd': 8}
assert result1 == 8
assert result2 == 3

# update
dx = {'a': 1, 'b': 2, 'c': 3}
db = {'d': 4, 'e': 5}
dx.update(db)  # 字典参数
dx.update(f=6)  # 关键字参数
dx.update(db, f=6, g=7)  # 混合参数
assert dx.get('f') == 6


# 字典的用途
temp = '姓名:%(name)s,年龄:%(age)3.0f,籍贯:%(location)s'
msg = {'name': 'JoJ', 'age': 23, 'location': '海拉尔群岛'}
print(temp % msg)

# 字典可以排序,在python3.6之后,但是之前不可以排序
dict_1 = {str(i): i for i in range(5)}
print(dict_1)
# 在运行效率上，{} 会比 dict() 快三倍左右