# -*- coding: utf-8 -*-
'''
@File    :   ini_configobj.py
@Time    :   2022/03/15 12:19:44

'''
import os

from configobj import ConfigObj


def get_path(filename):
    """ 创建一个配置文件，路径与本模块在同一个目录里面,example the filename 
    filename: test.init"""
    dirname = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dirname, filename)


path = get_path("test.ini")

config = ConfigObj(path, encoding='utf-8')


class MyConfigObj(object):
    def __init__(self, path, logger=None):
        if logger:
            self.logger = logger
        else:
            self.logger = print

        self.path = path
        self.conf = ConfigObj(self.path, encoding='utf8')
        # self.conf.filename = self.path

    def add_section(self, sec, option=None, value=None):
        self.conf[sec] = {}
        if option and value:
            self.conf[sec][option] = value
        self.conf.write()

    def remove_option(self, sec, option):
        del self.conf[sec][option]
        self.conf.write()

    def remove_section(self, sec):
        del self.conf[sec]
        self.conf.write()

    def save_other_file(self, path):
        self.conf.filename = path
        self.conf.write()
