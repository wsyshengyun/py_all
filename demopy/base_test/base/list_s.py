# coding:utf8

# 创建list
L = [1, 2, 3, 4, 5]
l2 = [None] * 5
l5 = [i for i in range(5)]  # 列表推导式
l3 = list('abc')
l33 = list(range(5))
l4 = 'a b c'.split(" ")

# 添加元素
# None<= insert(index)  在index的前面添加元素
l4.insert(1, 'element at 1 pos')  # 新添加的元素的位置在 索引1处，即在位置0后添加新元素

# 扩展列表
# list.extend(iterable) 参数为iterable类型, 在原来的列表上扩展, 输出：为None ,添加的列表的元素在最后面；
lit = ['a', 'b']
lit.extend(['x', 'y', 'z'])
lit.extend('mnk')
lit.extend((1,2,3))
lit.extend({11, 22, 33})
# list + list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
list4 = list1 + list2 + list3

# 删除元素
# pop(index) => element
ele1 = list4.pop(0)  # 弹出第1个元素
ele2 = lit.pop()  # 弹出最后一个元素

# None <= remove(element)
list4.remove(1) # 元素1不存在,报错 # 删除元素1，是值不是索引；如果有删除的元素有重复，则只会删除最前面的；

del lit[2] # 删除索引为2的元素，也即删除从前到后第3个元素

# 统计元素的个数方式
count_ = list4.count(1)

#  in 和 not in
bl = 'x' in lit

#  定位index方法；参数为具体元素的值，可选参数：切片范围
index = lit.index('x')

# 排序或反转列表
# None <==
lit.sort()  # 如果元素的类型不一样,会报错
lit = [5, 4, 3, 6, 9, 1]
lit.reverse()
lit.sort()
new_list = sorted(lit, reverse=True)


def list_remove_not_int(l):
    """
    在列表里面循环按条件删除一些元素在步骤为：
    1， 找出这些元素，放在一个新的列表里面
    2， 循环新的列表，依次在原列表里面删除这些元素。
    """
    del_lit = [ele for ele in l if not isinstance(ele, int)]
    for ele in del_lit:
        l.remove(ele)


list_remove_not_int(lit)

# 切片操作
#

lit = L.copy()
lit.insert(0, 0)
l1 = lit[::]  # lit 一样
# id一样么, 答案是不一样的
id1 = id(lit)
id2 = id(l1)
# L[:]
l2 = lit[:]
print(l2)  # == lit
print(id(lit) == id(l2))  # Flase

lit = [0, 1, 2, 3, 4, 5]
list2 = lit[::-1]  # lit的倒序
# L[a:b] => [a, b)  左闭右开
v3 = lit[:2]  # [0, 1]
v4 = lit[2:]  # [2, 3, 4, 5]
# 等效于 lit[-2+len:] => lit[4:]
# 也等效于: 从尾部向前2个元素
v5 = lit[-2:]  # [4, 5]
# 等效于: 除了尾部的两个元素之外的元素
v6 = lit[:-2]  # [0, 1, 2, 3]
v7 = lit[:0]  # []
v8 = lit[:1]  # [0]


# 切片增加步长
a = [1, 2]
b = [3, 4]
c = [5, 6]
d = sum((a, b, c), [])
# d = sum([a, b, c])  报错
assert d == [1, 2, 3, 4, 5, 6]
# s1 = sum(['a', 'b', 'c', 'e'], '') 报错


