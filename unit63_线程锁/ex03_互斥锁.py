#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_互斥锁.py"""

import threading
import time
number = 0
lock = threading.Lock()  # 创建互斥锁

def plus(lk):
    global number
    lk.acquire()  # 加锁
    for _ in range(1000000):
        number += 1
    print(f'{threading.current_thread().name} : {number}')
    lk.release()  # 释放锁

if __name__ == '__main__':
    threading.Thread(target=plus, args=(lock,)).start()
    threading.Thread(target=plus, args=(lock,)).start()
    time.sleep(1)
    print(f'{threading.main_thread().name} : {number}')
