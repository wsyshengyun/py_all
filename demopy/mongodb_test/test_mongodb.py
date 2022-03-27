# -*- coding: utf-8 -*-
'''
@File    :   test_mongodb.py
@Time    :   2022/03/27 23:07:23


'''

import unittest
from pymongo import MongoClient
import pymongo
from demopy.logger.log import logger
import datetime


class MyMongodbTest(unittest.TestCase):
    


    @classmethod
    def setUpClass(cls):
        #  创建数据库


        pass

    
    @classmethod
    def tearDownClass(cls):
        
        
        pass
    
    def setUp(self):
        
        logger.info("setup") 

        # 连接MongoDB
        self.client = MongoClient('localhost', 27017) 
        # client = MongoClient('mongodb://localhost:27017')

        # 指定数据库
        self.db = self.client['pythondb']   
        # db = client.pythondb    

        # 指定集合
        self.collection = self.db.students 
        # self.collection = db['students']

        

    
    def tearDown(self):

        remove = self.collection.remove() 
        logger.info("已经清空数据库,结果为{}".format(remove))
        
        pass
    
    
    
    

    
    def test_insert(self):
        
        student = {
            'id' : '20170101',
            'name' : 'jordan',
            'age' : 20,
            'gender' : 'male',
        }

        result = self.collection.insert(student) 
        logger.info("insert data result is :{}".format(result))
        
        pass
        
        
        
        
    
        
        