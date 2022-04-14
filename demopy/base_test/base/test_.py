# coding:utf-8

i = 0
while i < 5:
    i += 1
    if i == 3:
        break
else:
    i = 10
print(i)  # i = 3

#
i = 0
while i < 5:
    i += 1
    # if i == 3:
    #     break
else:
    i = 10
print(i)  # i = 10

# 迭代字典
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print("keys is {}".format(key))

for key, value in d.items():
    print("key is {}, ".format(key), "value is {}".format(value))

# 并行迭代
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for name, age in zip(names, ages ):
    print("name is {}, ".format(name), "age is {}".format(age))

# 迭代时获取索引
tsr = 'ni hao, wo shi wang'
for index, ts in enumerate(tsr):
    print(index, ts)


# 跳出循环
# break
# continue


