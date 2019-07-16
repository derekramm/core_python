#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_通过threading模块创建线程.py"""

import threading
import time
import random

def show():
    time.sleep(random.random())
    print(threading.current_thread().name, "is running....")

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=show)
        t.start()