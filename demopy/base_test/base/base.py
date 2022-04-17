# -*- coding: utf-8 -*-
'''
@File    :   base.py
@Time    :   2021/09/21 13:47:04
关于基本数据类型
'''

import sys 

x = '10' 
b = '16'
a = 10
bin_tsr = bin(a) 
hex_str = hex(a)
oct_str = oct(a)
print(int(bin_tsr,  2))   # 10 整数
print(int(hex_str,  16))  # 10 整数
print(int(oct_str,  8))  # 10 整数
print("0x16打印出来为： %s" % 0x16)
print("hex(16): %s" % hex(16))
print(" int('10', 10): %s" % int('10', 10))
print(" int(\"10\", 16): %s" % int('10', 16))

#=====================================列表 =======================================
print('\n')
lit = [1,2,3,4,5,6]
nlit = len(lit)
print("lit:  %s " % lit)
print("lit[1] : %s" % lit[1])
print( "lit(1 - len(lit)) : %s" % lit[1 - len(lit)])
print("lit[1]: %s" % lit[1])
print("lit[4]: %s" % lit[4])
print("lit[1:4] : %s" % (lit[1:4]))
print("lit[0:4] : %s" % (lit[0:4]))
print("lit[0:nlit] : %s" % lit[0:nlit])
print("lit[::] : %s" % (lit[::]))
print("id(lit) == id(lit[::]) : %s" % (id(lit) == id(lit[::])))
# 倒着切片
print("lit[-nlit:0] :%s" % (lit[-nlit:0]))

#=====================================字典=======================================
print('\n')
dit = {'a': 9, 'b':2, 'c':1, 'd':4, 'e':5, 'f':10, 'g':7, 'h':8}
# 排序

print("dit: %s" % dit)
print("按key排序: %s" % sorted(dit.items(), key=lambda d: d[0], reverse=True))
print("按value排序: %s" % sorted(dit.items(), key=lambda d: d[1], reverse=False))
# newlit = sorted(dit.items(), key=lambda d: d[1], reverse=False)
# print(newlit)
# print(dict(newlit))
print("dit.items() : %s" % list(dit.items()))


