# -*- coding: utf-8 -*-
'''
@File    :   ini_t.py
@Time    :   2022/03/15 08:50:11

英语  
section  - 节段、一段 
option - 选项
sender - 发送者  

ConfigParser 模块为常用的操作ini文件的模块，但是存在一些缺陷，无法识别section的大小写，无法读取文件注释，这样修带有注释的配置文件时就会存在问题。

'''
import configparser 
from ....logger.log import logger
import os 


curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, 'test.ini')
if not os.path.exists(cfgpath):
    logger.info("路径不存在")
    raise "not exists" 
logger.info('config path is : {}'.format(cfgpath))

# 创建管理对象
# conf = configparser.ConfigParser()
# 读取ini文件
# conf.read(cfgpath, encoding='utf8')  # python3 要加上encoding ； Python2不用加

def read_config():
    sections = conf.sections()
    logger.info('获取配置文件所有的section: {},  type is {}'.format(sections, type(sections)))


    # 获取所有的key
    options = conf.options(sections[0])
    logger.info('获取指定的sections:{} 下所有的option:{}'.format(sections[0], options))

    # items = conf.items('email_163')
    # logger.info('获取指定sections下所有的键值对: %s' % items)
    items = conf.items(sections[1])
    logger.info('获取指定sections: {} , 下所有的键值对: {}'.format(sections[1], items) )

    value = conf.get('email_163', 'sender')
    logger.info('获取指定的sections - {}, option - {}, value - {}'.format('email_163', 'sender', value))

def print_sections():
    logger.info("所有的字段：{}".format(conf.sections()))

def print_all_items():
    sections = conf.sections()
    for sec in sections:
        options = conf.options(sec)
        for key in options:
            value = conf.get(sec, key)
            logger.info("[{}]  {} = {} ".format(sec, key, value))

def write():
    conf.write(open(cfgpath, 'a', encoding='utf8'))
    pass



class MyConfigIni(object):
    def __init__(self, path, logger=None):
        self.path = path
        self.conf = configparser.ConfigParser()
        if logger:
            self.logger = logger
        
        self.logger.info("path : {}".format(self.path))
        pass


    def conf(self):
        return self.conf
    
    
    def read(self):
        self.conf.read(self.path, encoding='utf-8')

    def get_sections(self):
        return self.conf.sections()
    
    def write(self, mode = 'w'):
        self.conf.write(open(self.path, mode, encoding='utf8'))
    

    def add_section(self, sec):
        """ 添加section，添加前检查 """
        if self.conf.has_section(sec):
            self.logger.info("add {} is failed, section is exists!".format(sec))
        else:
            self.conf.add_section(sec)
            self.write()
        pass

    def remove_section(self, sec):
        """ 删除section """
        if self.conf.has_section(sec):
            self.conf.remove_section(sec)
            self.write()
        else:
            self.logger.warn("remove {sec} is failed! section is not exists! ".format(sec))

    def add_option(self, sec, option, value):
        """ add option """
        if not self.conf.has_option(sec, option):
            self.conf.set(sec, option, value)
            self.write()
        else:
            self.logger.warn("add option: {} is failed, this is exists!".format(option))

        
        self.conf.set(sec, key, value)
    
    def remove_option(self, sec, option):
        """ remove option """
        if self.conf.has_option(sec, option):
            flg = self.conf.remove_option(sec, option)
            self.write()
            self.logger.info("remove option:{} is success, return value is {}".format(option, flg))
        else:
            self.logger.warn("remove {} is failed, this option is not exists!".format(option))

    
    def modify_value(self, sec, option, value):
        self.conf.set(sec, option,value=value)
        self.write(mode='r+')


    def print_sections(self):
        """ logging sections """
        self.logger.info("所有的字段：{}".format(self.conf.sections()))
        
    def print_all_items(self):
        """ logging items """
        sections = self.get_sections()
        self.logger.info(sections)
        for sec in sections:
            options = self.conf.options(sec)
            for key in options:
                value = self.conf.get(sec, key)
                self.logger.info("[{}]  {} = {} ".format(sec, key, value))
        
    
    
    
def test():
    obj = MyConfigIni(cfgpath, logger=logger)
    obj.read()
    # obj.add_section("Sheng")
    # obj.add_option('Sheng', 'xiancheng1', "xinye")
    # obj.modify_value("Sheng", 'xiancheng1', 'xindianpu')
    # obj.add_section("SHI")
    # obj.add_option("SHI", "xiancheng2", 'xinye')
    # obj.remove_section('SHI')
    obj.remove_option("Sheng", 'xiancheng1')

    pass

test()
# read_config()


# -----------------------------------------------------------
# 删除一个字段
# 线程一个key
# -----------------------------------------------------------

# -----------------------------------------------------------
# 增加一个字段
# conf.add_section('person')
# 增加一个key 和一个值  
# conf.set('person', 'name', '汪生云')
# conf.set('person', 'age', '35')
# conf.set('person', 'sex', '男')
# 增加一个key， 不增加值可以么

# 写入文件
# write()

# 打印输出
# print_sections()
# print_all_items()
# -----------------------------------------------------------
# -----------------------------------------------------------
#  写入文件 
# -----------------------------------------------------------