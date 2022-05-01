# coding:utf8

"""
list 的使用
"""
# 创建list
L = [1, 2, 3, 4, 5]
l2 = [None] * 5
l3 = list('abc')
l4 = 'a b c'.split(" ")
# 列表推导式
l5 = [i for i in range(5)]

# 添加元素
# None<= insert(index)  在index的前面添加元素
l = [1, 2, 3, 4, 1]
lit = l.copy()
lit.insert(1, 'insert at 1')  # 新添加的元素的位置在 索引1处，即在位置0后添加新元素
assert lit[1] == 'insert at 1'

# 扩展列表
# list.extend(iterable) 参数为iterable类型
# 在原来的列表上扩展；
# 输出：为None
# 添加的列表的元素在最后面；
lit = ['a', 'b']
# lit = lit.extend(['x', 'y', 'z'])  错误, lit.extend后返回了自己
reslut = lit.extend(['x', 'y', 'z'])
# ['a', 'b', 'x', 'y', 'z', 'm', 'n', 'k']
lit.extend('mnk')

#
# 删除元素
# 
lit = L.copy()

# pop(index) => element
# 弹出第1个元素
ele1 = lit.pop(0)

# 弹出最后一个元素
ele2 = lit.pop()

# None <= remove(element)
# 删除元素1，是值不是索引；如果有删除的元素有重复，则只会删除最前面的；
# lit.remove(1)  元素1不存在,报错
lit = L.copy()
lit.remove(1)

# 删除索引为2的元素，也即删除从前到后第3个元素
# lit[index] 返回的是第 index+1 个元素
del lit[2]

# 统计元素的个数方式
lit = L.copy()
lit.append('x')
lit.append('x')
count_ = lit.count('x')  # 2

#  in 和 not in
bl = 'x' in lit

#  定位index方法；参数为具体元素的值，可选参数：切片范围
index = lit.index('x')

# 排序或反转列表
# return None
lit.reverse()


# 直接更改了原列表
# 有三个默认 参数cmp=None,key=None,reverse=False
# 如果元素的类型不一致，不能排序

#  下面不能完全删除连续的字符元素
# def list_remove_not_int(lit):
#     for ele in lit:
#         if not isinstance(ele, int):
#             lit.remove(ele)
#         pass

def list_remove_not_int(lit):
    """
    todo 列表里面删除一些元素,还有哪些方法呢?
    """
    del_lit = [ele for ele in lit if not isinstance(ele, int)]
    for ele in del_lit:
        lit.remove(ele)


list_remove_not_int(lit)
lit.sort()

new_lit = sorted(lit)
# 两个的身份不一样的
id_new_lit = id(new_lit)
id_lit = id(lit)

# 切片操作
lit = L.copy()
lit.insert(0, 0)
v1 = lit[::]  # lit 一样

# id一样么, 答案是不一样的
id1 = id(lit)
id2 = id(v1)

v2 = lit[::-1]  # lit的倒序
# [0, 1]
v3 = lit[:2]
# [2, 3, 4, 5]
v4 = lit[2:]
# [4, 5]
v5 = lit[-2:]
# [0, 1, 2, 3]
v6 = lit[:-2]

# 切片增加步长

pass

