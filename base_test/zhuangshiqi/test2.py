# codeing:utf8

'''
װ����  
    )))��������һ������
    )))�������������Ĺ��ܶ����޸������
    )))Ϊ�Ѿ����ڵĻ���� ��Ӷ���Ĺ���  
    )))����ֵ   Ҳ��һ����������  
    )))������?? 
'''


def debug(func):
    def wrapper(something):
        pass
        return func(something)
    return wrapper 

@debug
def say_hello():
    print("hello")


say_helloi()

