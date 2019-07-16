#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_事件锁.py"""

import random
import threading
import time

def get_name():
    return random.choice([chr(c) for c in range(65, 92)])

event = threading.Event()

def lighter():
    green_time = 3
    red_time = 3
    event.set()
    while True:
        print("\33[32;0m 绿灯亮...\033[0m")
        time.sleep(green_time)
        event.clear()
        print("\33[31;0m 红灯亮...\033[0m")
        time.sleep(red_time)
        event.set()

def run(name):
    while True:
        if event.is_set():
            print(f'{name} 通过了马路')
            time.sleep(random.randint(1, 5))
        else:
            print(f'{name} 看到红灯，在路边等待')
            event.wait()
            print(f'{name} 看到绿灯，通过了马路')

if __name__ == '__main__':
    light = threading.Thread(target=lighter, )
    light.start()

    for name in ['小铭', '大蜥蜴']:
        car = threading.Thread(target=run, args=(name,))
        car.start()
