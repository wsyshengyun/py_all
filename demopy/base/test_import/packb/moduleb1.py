# -----------------------------------------------------------
# 以下两句import导入都是正确的 一个相对导入,一个绝对导入;
# -----------------------------------------------------------
# from .packc.modulec1 import c1
# from packb.packc.modulec1 import c1



print("in moduleb1.py")

b1 = 1000

def moduleb1_fun():
    print("in moduleb1_fun")

# print("in b1, c1 value is ： %s" % c1)