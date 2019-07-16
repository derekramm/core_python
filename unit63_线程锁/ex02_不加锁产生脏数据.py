#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_不加锁产生脏数据.py"""

import threading
import time
number = 0

def plus():
    global number
    for _ in range(1000000):
        number += 1
    print(f'{threading.current_thread().name} : {number}')

if __name__ == '__main__':
    threading.Thread(target=plus).start()
    threading.Thread(target=plus).start()
    time.sleep(1)
    print(f'{threading.main_thread().name} : {number}')
