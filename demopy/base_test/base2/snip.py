# coding:utf8
import sys

print(sys.argv)
if isinstance(sys.argv, list):
    print("列表的长度是: {}".format(len(sys.argv)))

# for ... else
for i in range(5):
    print(i)
    if i == 2:
        print('break for')
        break
else:
    print('else')

print('-'*50)
a = 5
while a>0:
    print(a)
    a -= 1
    if a == 2:
        print('break')
        break
else:
    print('else')
