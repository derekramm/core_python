#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_信号锁.py"""

import threading
import time
import random
semaphore = threading.BoundedSemaphore(3)

def enter(name, se):
    se.acquire()
    print(f'{name} is enter')
    time.sleep(3)
    se.release()

def get_name():
    return random.choice([chr(c) for c in range(65, 92)])

if __name__ == '__main__':
    for i in range(20):
        threading.Thread(target=enter, args=(get_name(), semaphore)).start()
