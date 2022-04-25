# -*- coding: utf-8 -*-
'''
@File    :   test_mongodb.py
@Time    :   2022/03/27 23:07:23


'''

import unittest

from pymongo import MongoClient

from demopy.logger.log import logger


class MyMongodbTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        #  创建数据库
        logger.info("setUpClass")

        # 连接MongoDB
        cls.client = MongoClient('localhost', 27017)
        # client = MongoClient('mongodb://localhost:27017')

        # 进入数据库方法1 
        cls.db = cls.client['dbtest']
        # 进入数据库方法2
        # db = client.pythondb     

        # 指定集合
        # cls.collection = cls.db.my_db 
        cls.collection = cls.db['t1']

        # all_dbs = cls.client.database_names() 

        # logger.info("cls.collection : {}".format(cls.collection))
        # logger.info("cls.db: {}".format(cls.db))
        # logger.info("cls.collection {}".format(cls.db.collection_names()))

        pass

    @classmethod
    def tearDownClass(cls):

        # TODO 关闭数据库连接??

        # result = cls.collection.delete_many({})
        # logger.info("清除的数据个数: {}".format(result.deleted_count))
        logger.info("tearDownClass")
        pass

    def setUp(self):
        # logger.info("开始插入数据~")
        student = {'id': '20170101', 'name': 'jordan', 'age': 20, 'gender': 'male'}
        sts = [{'id': '20170102', 'name': 'wsy', 'age': 30, 'gender': 'women'},
               {'id': '20170108', 'name': 'wudandan', 'age': 35, 'gender': 'woman'},
               {'id': '20170103', 'name': 'lrf', 'age': 40, 'gender': 'male'},
               {'id': '20170104', 'name': 'lx', 'age': 50, 'gender': 'male'},
               {'id': '20170109', 'name': 'liuxiaojun', 'age': 56, 'gender': 'male'},
               {'id': '20170105', 'name': 'pdm', 'age': 60, 'gender': 'male'},
               {'id': '20170106', 'name': 'll', 'age': 70, 'gender': 'women'},
               {'id': '20170107', 'name': 'shuaige', 'age': 80, 'gender': 'male'},
               ]
        # result = self.collection.insert_one(student) 
        results = self.collection.insert_many(sts)
        ids = results.inserted_ids
        # logger.info("insert_many ids  len {}".format(len(ids))) 
        pass

    def tearDown(self):

        result = self.collection.delete_many({})
        # logger.info("清除的数据个数: {}".format(result.deleted_count))
        pass

    def test_insert(self):

        self.assertEqual(self.collection.estimated_document_count(), 8)

        per = {'name': 'liuqiangdong', 'age': 44, 'gender': 'male'}
        self.collection.insert_one(per)

        self.assertEqual(self.collection.estimated_document_count(), 9)

        result = self.collection.find_one({'name': 'liuqiangdong'})

        logger.info("result = {}".format(result))

        pass

    @unittest.skip
    def test_all_dbs_collections(self):

        logger.info("test_all_dbs_collections")
        all_dbs = self.client.list_database_names()
        for db_name in all_dbs:
            db = self.client[db_name]
            coll = db.list_collection_names()
        pass

    def test_find(self):

        result = self.collection.find({})
        len_ = len(list(result))
        self.assertEqual(len_, 8)
        pass

    def test_find_one(self):

        result = self.collection.find({'name': 'wsy'})

        pass

    def test_find_many(self):

        results = self.collection.find({'age': {'$gt': 40}})
        names = [objdit['name'] for objdit in list(results)]
        # names_age_gt_40 = ['lx', 'pdm', 'll', 'shuaige', 'liuxiaojun']
        # self.assertEqual(names, names_age_gt_40)

        # for per in results:
        # logger.info("per = {}".format(per))

    def test_find_many_fuhe(self):

        result = self.collection.find({'age': {'$lt': 60}}, {'gender': 'male'})
        # logger.info("158 : {}".format(result.matched_count))
        for obj in result:
            logger.info("obj is :{}".format(obj))
        pass

    def test_update_name(self):
        result = self.collection.update_one({'name': 'wsy'},
                                            {'$set': {'name': 'wangshengyun'}})
        logger.info("原始的文档 : {}".format(result.raw_result))

        result = self.collection.find_one({'name': 'wangshengyun'})
        self.assertIsNotNone(result)

        result = self.collection.find_one({'name': 'wangxiaoyu'})
        self.assertIsNone(result)

    def test_update_many(self):

        result = self.collection.update_many({},
                                             {'$inc': {'age': 1}})
        matched_count = result.matched_count
        modified_count = result.modified_count
        logger.info("matched_count:{} , modified_count:{}".format(matched_count, modified_count))
        pass

    def test_update_inc(self):

        condition = {'name': 'wsy'}
        result = self.collection.update_many(condition, {'$inc': {'age': 1}})
        # logger.info("{}".format(result.matched_count))
        # TODO:result对象有什么方法和属性,可以得到更新的对象么?

        age = self.collection.find_one(condition)['age']
        self.assertEqual(age, 31)

        pass

    def test_delete_one(self):

        # result = self.collection.delete_one({})
        # logger.info("199 result = {}".format(result.deleted_count))

        result = self.collection.delete_one({'name': 'liuqingd'})
        logger.info("199 result = {}".format(result.deleted_count))
        # TODO 如何判断删除成功
        pass

    def test_delete_filter(self):

        results = self.collection.delete_many({'age': {'$gt': 30, '$lt': 70}})
        logger.info("210 results.deleted_count = {}".format(results.deleted_count))
        # TODO 如何得到删除的对象,得到他们的id或者别的属性. 
        pass
