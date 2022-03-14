# -*- coding: utf-8 -*-
'''
@File    :   test1.py
@Time    :   2020/09/23 22:27:06
'''

""" 
全局变量与局部变量重名的情况下  
如果函数内的局部变量只是引用的话  和  全局变量是一样的  

如果函数内的局部变量重新赋值的话  是一个的新的变量  它们的id是不一样的   \
    必须要加上  global 关键词  

 """
b = 1

print("global b-id is : %d" % id(b))
def fun():
    b = 2
    print("fun b-id is : %d" % id(b))


if __name__ == '__main__':
    fun()
    


    