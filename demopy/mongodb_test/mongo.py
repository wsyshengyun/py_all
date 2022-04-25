# -*- coding: utf-8 -*-
'''
@File    :   testmongo.py
@Time    :   2020/10/22 11:12:14
'''

import pymongo

" 连接pymongo服务 "
from pymongo import MongoClient

client = MongoClient()

""" 连接数据库 """

# db = client.my_db 
db = client['my_db']

# 建表  
# collection = db.my_collection 
collection = db['my_collection']

names = db.collection_names()
print(names)

# insert
data = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
}

flag_insert = False
if flag_insert:
    collection.insert_one(data)

new_document = [
    {'x': 3}, {'x': 4}
]

if flag_insert:
    result = collection.insert_many(new_document)

# find
one = collection.find_one()
print(one)


def print_all_mongo():
    for item in collection.find():
        print(item)


def print_():
    print('=' * 30)


print_all_mongo()
print_()

# count 
counts = collection.find().count()
print("count == %d" % counts)

# sort 
collection.find().sort('key1')  # 默认为升序
result = collection.find().sort('key1', pymongo.ASCENDING)  # 升序 a scending
print('result==', result)
print_all_mongo()
print_()
collection.find().sort('key1', pymongo.DESCENDING)  # 降序de scending
print_all_mongo()
