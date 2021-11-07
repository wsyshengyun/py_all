''' 
list 的使用
'''
# 创建list  
lit = [1,2,3,4,5]
lit1 = [None] * 5
print(lit1)
# 列表推导式
print('列表推导式创建：', [i for i in range(5)])
# 添加元素
lit.append(1)
print(lit)
lit.insert(1, 'insert at 1')
print(lit)
lit.pop(0)
print('pop(0): {}'.format(lit))
lit.pop()
print('pop(): {}'.format(lit))


