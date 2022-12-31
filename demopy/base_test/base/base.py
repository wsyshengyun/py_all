# -*- coding: utf-8 -*-


x = '10'
b = '16'
a = 10
bin_tsr = bin(a)
hex_str = hex(a)
oct_str = oct(a)
print(int(bin_tsr, 2))  # 10 整数
print(int(hex_str, 16))  # 10 整数
print(int(oct_str, 8))  # 10 整数
print("0x16打印出来为： %s" % 0x16)
print("hex(16): %s" % hex(16))
print("int('10', 10): %s" % int('10', 10))
print("int(\"10\", 16): %s" % int('10', 16))
