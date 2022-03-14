# -*- coding: utf-8 -*-
'''
@File    :   server.py
@Time    :   2021/09/22 22:22:53
'''

import sock_alladdress as sock 

obj = sock.MySocketServer('127.0.0.1', 9999)
obj.start()
