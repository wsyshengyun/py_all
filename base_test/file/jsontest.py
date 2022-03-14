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


#=====================================loads方法=======================================
path = './dd.json'
f = open(path, encoding='utf-8')
content = f.read()  
user_dic = json.loads(content)
# print(user_dic)
f.close() 



#=====================================load方法 =======================================
print('*'*50)
f= open(path, encoding='utf-8')
user_dic = json.load(f) 
# print(user_dic)
f.close()  

#=====================================字典转换成json=======================================
""" dumps()方法 
 """
stus = {
    'xiaojun': '123456', 
    'xiaohei': '7891',
    'abc' : '1111'
}

res2 = json.dumps(stus, indent=8, ensure_ascii=False)
print(res2)
print(type(res2))  # 还是一个字符串类型 ；  json样式的字符串

path_dump = './dump.json'
with open(path_dump, 'w', encoding='utf-8') as f:
    f.write(res2)

#=====================================字典转换为json=======================================
f = open(path_dump, 'w', encoding='utf-8')
json.dump(stus, f, indent=8, ensure_ascii=False)









