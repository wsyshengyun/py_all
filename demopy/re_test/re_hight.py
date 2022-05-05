# coding:utf8

import re

"""
.	匹配除换行符以外的任意字符
\w	匹配字母或数字或下划线或汉字
\s	匹配任意的空白符
\d	匹配数字
\b	匹配单词的开始或结束
^	匹配字符串的开始
$	匹配字符串的结束

"""


# \|\|\|\|\|\|\|\|\|\|\|\|\|正整数|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

def match(pattern, tsr):
    return re.match(pattern, tsr)


def match_group_iter(pattern, tsr):
    result: re.Match = match(pattern, tsr)
    if result.lastindex:
        for i in range(1, result.lastindex+1):
            yield result.group(i)


def match_group_list(pattern, tsr):
    iter = match_group_iter(pattern, tsr)
    return list(iter) if iter else None


pattern = r"^[1-9]\d*$"
assert match(pattern, '899')

ret1 = re.match(r"\w*?(\d+)\w+?(\d+)\w+", 'aa00bb11cc')
# ret1 = re.match(r"\w*?\d+\w+?\d+\w+", 'aa00bb11cc')
res = match_group_list(r"\w*?(\d+)\w+?(\d+)\w+", 'aa00bb11cc')
print(res)
# v0 = ret1.group(0)
# v1 = ret1.group(1)
# v2 = ret1.group(2)

#
# 匹配中文
#
pstr = r'[\u4e00-\u9fa5]{5}'  # # 匹配了5个汉字
pstr = r'[\u4e00-\u9fa5]+'  # # 贪婪匹配
pstr = r'[\u4e00-\u9fa5]*'  # # todo 为什么是惰性匹配
ret = re.search(pstr, "aa123我是中国人")
print(ret.group())


pass
