# -*- coding: utf-8 -*-
'''
@File    :   test_getip.py
@Time    :   2021/10/03 11:28:40

'''

import socket, platform 

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('www.baidu.com', 0))
        ip = s.getsockname()[0] 
    except:
        ip = '0.0.0.0'
    finally:
        s.close() 
    return ip

if __name__ == "__main__":
    sys_type = platform.system()
    print("本机的系统类型为：{}".format(sys_type))
    """ 输出本机的IP  """
    print("socket.gethostname() -> {}".format(socket.gethostname()))
    # print("socket.gethostname() -> {}".format(socket.gethostname()))


    if sys_type == "Windows" or "Darwin":
        ip_address = socket.gethostbyname(socket.gethostname())
        print("本机的IP：{}".format(ip_address))
    elif sys_type == "Linux":
        ip_address = get_ip()
        print("本机的IP：{}".format(ip_address))
    else:
        print("其他系统")