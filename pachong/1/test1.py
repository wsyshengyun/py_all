# -*- coding: utf-8 -*-
'''
@File    :   test1.py
@Time    :   2020/09/22 17:19:50
'''

path = './file_requests.txt'
with open(path, 'r') as f:
    file_text = f.read() 
sep = '\n'

# create dict 
#=====================================第一种写法 =======================================
lines = file_text.split(sep)
dit = {}
for line in lines:
    key,value = line.split(': ')
    dit[key] = value


#=====================================另一种写法 简单=======================================
dit = dict(line.split(": ") for line in file_text.split(sep))

#=====================================打印dict=======================================
# print dit 
for key in dit:
    print(key, ": ", dit[key])