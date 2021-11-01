# -*- coding: utf-8 -*-
'''
@File    :   ip.py
@Time    :   2021/09/22 22:56:27
'''


from IPy import IP 
ip = IP('127.0.0.0/30')
# for x in ip:
    # print(x)

print("ip.reverseNames() = {}".format(ip.reverseNames()))
print("ip.iptype() = {}".format(ip.iptype()))
vs = IP('10.0.0.0/8').version()
print("IP('10.0.0.0/8').version() = {}".format(vs))
vs6 = IP('::1').version()
print("IP('::1').version() = {}".format(vs6))
print("IP('0x7f000001') = {}".format(IP('0x7f000001')))