# -*- coding: utf-8 -*-
'''
@File    :   second.py
@Time    :   2021/11/14 15:42:16
进阶
'''
import os
import logging
import uuid
from logging import Handler, FileHandler, StreamHandler


class PathFileHandler(FileHandler):
    def __init__(self,path, filename, mode='a', encoding=None, delay=False):
        # filename = os.fspath(filename)
        filename = os.path.join(path,filename)
        if not os.path.exists(filename):
            os.mkdir(path)
        self.baseFilename = os.path.join(path, filename)
        self.mode = mode 
        self.encoding = encoding
        self.delay = delay
        if delay:
            Handler.__init__(self)
            self.stream = None 
        else:
            StreamHandler.__init__(self, self._open())


class Loggers(object):
    """ 
    uuid 在不停的变，每次运行一次就改变一次，造成运行一次就会创建一个新的名字。
    """
    #日志级别关系的映射
    level_relations = {
        'debug':logging.DEBUG, 
        'info':logging.INFO, 
        'warning':logging.WARNING, 
        'error':logging.ERROR, 
        'critical':logging.CRITICAL, 
    }

    def __init__(self, filename='{uid}.log'.format(uid=uuid.uuid4()),
                level='info', log_dir='log'
                ,fmt='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'):

        self.logger = logging.getLogger(filename)
        abspath = os.path.dirname(os.path.abspath(__file__))
        self.directory = os.path.join(abspath, log_dir)
        format_str = logging.Formatter(fmt) # 设置日志的格式
        self.logger.setLevel(self.level_relations.get(level)) # 设置日志的级别
        stream_handler = logging.StreamHandler() # 往屏幕上输出
        stream_handler.setFormatter(format_str)
        file_handler = PathFileHandler(path=self.directory, filename=filename, mode='a')
        file_handler.setFormatter(format_str)
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

if __name__ == '__main__':
    txt = 'nihao'
    log = Loggers(level='debug')
    log.logger.info(4)
    log.logger.info(5)
    log.logger.info(txt)

    pass
