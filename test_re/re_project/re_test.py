# -*- coding: utf-8 -*-

'''
@File    :   re_test.py
@Time    :   2021/01/19 23:12:57
'''


import re 
import inspect



def lambda_to_expr_str(lambda_fn):
    """c.f. https://stackoverflow.com/a/52615415/134077"""
    if not lambda_fn.__name__ == "<lambda>":
        raise ValueError('Tried to convert non-lambda expression to string')
    else:
        lambda_str = inspect.getsource(lambda_fn).strip()
        expression_start = lambda_str.index(':') + 1
        expression_str = lambda_str[expression_start:].strip()
        if expression_str.endswith(')') and '(' not in expression_str:
            # i.e. l = lambda_to_expr_str(lambda x: x + 1) => x + 1)
            expression_str = expression_str[:-1]
        print(expression_str , ":  ", lambda_fn())
        # return expression_str

s = 'hello, world'
regex = re.compile("345", re.I)
result = regex.search("0123456789")
lambda_to_expr_str(lambda:result.string)
lambda_to_expr_str(lambda:result.endpos)
lambda_to_expr_str(lambda:result.re)
lambda_to_expr_str(lambda:result.end())
lambda_to_expr_str(lambda:result.lastgroup)
lambda_to_expr_str(lambda:result.lastindex)





