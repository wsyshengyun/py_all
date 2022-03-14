# -*- coding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/09/22 22:07:58
'''

path = './html.html'
with open(path, encoding='utf-8') as f:
    text = f.read()

from lxml import etree 

obj = etree.HTML(text)
result = obj.xpath("//div/a/text()")
# result = obj.xpath("//div/a[contains(@data-hovercard-type, 'user')]")
# result = obj.xpath("//div//text()")
for ele in result:
    print(ele)
