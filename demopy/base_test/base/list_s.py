''' 
list 的使用
'''
# 创建list  
l1 = [1, 2, 3, 4, 5]
l2 = [None] * 5
l3 = list('abc')
l4 = 'abc'.split('')
# 列表推导式
l5 = [i for i in range(5)]

# 添加元素
l = [1, 2, 3, 4]
l.append(1)  # 在列表之后添加元素
l.insert(1, 'insert at 1')  # 新添加的元素的位置在 索引1处，即在位置0后添加新元素

# 扩展列表
# list.extend(iterable) 参数为iterable类型
# 在原来的列表上扩展；
# 输出：为None
# 添加的列表的元素在最后面；
lit = ['a', 'b']
lit = lit.extend(['x', 'y', 'z'])
lit.extend('mnk')

#
# 删除元素
# 


lit.pop(0)  # 弹出第1个元素

lit.pop()  # 弹出最后一个元素

lit.remove(1)  # 删除元素1，是值不是索引；如果有删除的元素有重复，则只会删除最前面的；

del lit[2]  # 删除索引为2的元素，也即删除从前到后第3个元素

# 统计元素的个数方式
print('x的个数为：', lit.count('x'))

#  in 和 not in
print(" {}".format('y' in lit))

#  定位index方法；参数为具体元素的值，可选参数：切片范围
print('x的索引是： {}'.format(lit.index('x')))

# 排序或反转列表
lit.reverse()

lit.sort()  # 如果元素的类型不一致，不能排序
# 有三个默认 参数cmp=None,key=None,reverse=False
# 直接更改了原列表


# 切片操作
