

# -----------------------------------------------------------
# dict的创建方法 
# -----------------------------------------------------------

# 直接赋值
dit1 = {}  

# 直接赋值
dit3 = {'a':1, 'b':2, 'c':3}
print(dit3)

# dict()方式
dict1 = dict()

# dict(**kwargs)
dit1 = dict(a=1, b=2 ,c=3)  # 通过关键字参数的方法创建
print(dit1)


# 通过循环赋值的方法创建字典
    # 创建一个可迭代对象的列表
lit = [('name','jonah'), ('age', 14)]
dic1 = {}
for k,v in lit:
    dic1[k] = v


# 直接通过可迭代对象生成字典 dict(iterable)
lit = [('name','jonah'), ('age', 14)]
dic2 = dict(lit)
print(dic2)


# fromkeys方式
dit6 = dict.fromkeys(['a', 'b', 'c'], 5) 
print(dit6)



# dict + key 
d1 = {'a':1, 'b':2}
d2 = dict(d1, c=3)
print(d2)

# 生成式方式
d1 = {i:chr(i) for i in range(65,69)}
print(d1)

# dict(mapping)  -- zip 方式
dit5 = dict(zip(['a', 'b', 'c'], [1,2,3,]))
print(dit5)

# dict(mapping)  -- map 方式
mp = map(lambda x,y: (x,y), 'ABCD', range(1,5))
dit = dict(mp)
print(dit)
