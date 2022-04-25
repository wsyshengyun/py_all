# -*- coding: utf-8 -*-
'''
@File    :   th_event.py
@Time    :   2021/10/02 19:37:53
Event类的应用: 模拟红绿灯
'''

import threading
import time

event = threading.Event()


def lighter():
    green_time = 8  # green light's time
    red_time = 8
    event.set()  # 初始设置为绿灯
    while True:
        print("绿灯亮。。。\n")
        time.sleep(green_time)
        event.clear()

        print("红灯亮。。。\n")
        time.sleep(red_time)
        event.set()


def run(name):
    while True:
        if event.is_set():  # 判断当前是否为放行状态
            print("一辆{} 呼啸而过。。。\n".format(name))
            time.sleep(2)
        else:
            print("一辆{}开来，看到红灯，无奈的停下了。。\n".format(name))
            event.wait()
            print("{} 看到绿灯亮了，瞬间飞起。。。\n".format(name))


lighter = threading.Thread(target=lighter)
lighter.start()

for name in ['奔驰', '宝马', '奥迪']:
    car = threading.Thread(target=run, args=(name,))
    car.start()
