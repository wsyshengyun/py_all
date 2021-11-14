# -*- coding: utf-8 -*-
'''
@File    :   first.py
@Time    :   2021/11/14 15:25:53
logging test
'''
import logging


# 修改默认级别，并修改log文件的地址
# 默认的级别是DEBUG
logging.basicConfig(level=logging.DEBUG, filename='coder.log', filemode='a')

logging.debug("崔庆才 | 静觅， 韦世东 | 奎因")
logging.warning("邀请你关注微信公众号【进击Coder】")
logging.info('和大佬 一起coding、共同进步')
