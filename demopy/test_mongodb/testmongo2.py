# -*- coding: utf-8 -*-
'''
@File    :   testmongo2.py
@Time    :   2020/10/25 21:36:52
'''

import pymongo
# 连接数据库
# myclient = pymongo.MongoClient(host='127.0.0.1', port=27017)
myclient = pymongo.MongoClient(host='localhost', port=27017)
db = myclient['dbtest']
my_set = db['t1']

data = {'name' : 'zhangsan', 'age':18}

flg_insert = False
if flg_insert:
    my_set.insert(data)
    my_set.save(data)

# insert many 
users = [
    {'name':'zhangsan1' ,'age':19}, 
    {'name':'lisi', 'age':20}, 
    {'name':'dabao' ,'age':22}, 
]

if flg_insert:
    my_set.insert_many(users)



# search  
def output1():
    for i in my_set.find():
        print(i)
    for i in my_set.find({'name':'zhangsan'}):
        print(i)
    print("-" * 30)
    print(my_set.find_one({'name':'zhangsan'}))

# 2020年10月27日
from student import one_student, many_students 
def insert_2():
    my_set.insert_one(one_student) 
    my_set.insert_many(many_students)
    pass

# insert_2()
def print_results(result):
    for ele in result:
        print(ele)
def output_2():
    result = my_set.find_one()
    print(result)

def find_all_2():
    condition = {'male':'man'}
    result = my_set.find(condition)
    print_results(result)


from bson import ObjectId
def find_from_id():
    condition = {'_id': ObjectId("5f980f1cbdf30eee28d323db")}
    result = my_set.find_one(condition) 
    print(result)


def sort_age(results):
    condition = 'age', pymongo.ASCENDING
    condition = 'age', pymongo.DESCENDING
    resultsed = results.sort(*condition)
    return resultsed

def find_1():
    condition = {'age':{'$gte':22}}
    result = my_set.find(condition)
    result = sort_age(result)
    print_results(result)

def find_2():
    condition = {'name':{'$regex':'^d.*'}}
    condition = {'name':{'$regex':'.*a.*'}}
    result = my_set.find(condition) 
    print_results(result)


find_2()
# find_from_id()

# output_2() 
# find_all_2()









