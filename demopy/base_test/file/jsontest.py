# -*- coding: utf-8 -*-
'''
@File    :   jsontest.py
@Time    :   2020/09/25 19:46:55
'''

""" 
json是一种通用的数据类型
一般情况下接口返回的数据类型都是json
长得像字典，形式也是k-v{ }
其实json是字符串
字符串不能用key、value来取值，所以要先转换为字典才可以
 """

""" 
 json格式key： 要用双引号
 文件里面注释不能用  #  
 :load(f) 传的是文件对象   
 :loads(tsr)  需要先读取文件内容后再使用 | 传的是字符串
 不管是dump还是load，带s的都是和字符串相关的，不带s的都是和文件相关的。
"""
import json

# =====================================loads方法=======================================
path = './dd.json'
f = open(path, encoding='utf-8')
content = f.read()
user_dic = json.loads(content)
# print(user_dic)
f.close()


def translate_obj_from_json(values):
    val = json.loads(values)
    print(val)
    return val


values = '1'
val = translate_obj_from_json(values)
values = '"nihao"'  # 不能写成"nihao" 或者'nihao'
val = translate_obj_from_json(values)
values = "1"
val = translate_obj_from_json(values)
pass

# =====================================load方法 =======================================
print('*' * 50)
f = open(path, encoding='utf-8')
user_dic = json.load(f)
# print(user_dic)
f.close()

# =====================================字典转换成json=======================================
""" dumps()方法 
 """
stus = {
    'xiaojun': '123456',
    'xiaohei': '7891',
    'abc': '1111'
}

res2 = json.dumps(stus, indent=8, ensure_ascii=False)
print(res2)
print(type(res2))  # 还是一个字符串类型 ；  json样式的字符串

path_dump = './dump.json'
with open(path_dump, 'w', encoding='utf-8') as f:
    f.write(res2)


def dump_to_tsr(obj):
    tt = json.dumps(obj)
    print(tt)
    return tt


obj = 'nihao'
val = dump_to_tsr(obj)
obj = '1'
val = dump_to_tsr(obj)
obj = 222
val = dump_to_tsr(obj)

# =====================================字典转换为json=======================================
f = open(path_dump, 'w', encoding='utf-8')
json.dump(stus, f, indent=8, ensure_ascii=False)


def dump_class_obj():
    class A:
        def __init__(self, a=1):
            """ """
            print("__init__")
            self.a = a

    obj = A()
    tsr = json.dumps(obj)
    print(tsr)


# dump_class_obj()
pass

print(
    '-'*50
)
from demopy.base_test.base import test_snip
print(dir(test_snip))
