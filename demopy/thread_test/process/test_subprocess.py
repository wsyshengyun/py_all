# -*- coding: utf-8 -*-
'''
@File    :   test_subprocess.py
@Time    :   2020/11/12 07:47:07
'''

import subprocess

# pingP = subprocess.Popen(args='ping -n 4 www.sina.com.cn', shell=True) 
pingP = subprocess.Popen(args='ping -n 4 www.sina.com.cn', shell=True
                         , stdout=subprocess.PIPE)
pingP.wait()
bstr = pingP.stdout.read()
# print(bstr.encode('utf-8'))
print(pingP.pid)
print(pingP.returncode)
