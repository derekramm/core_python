#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_创建线程时传入参数.py"""
import threading
import time
import random

def show(name):
    time.sleep(random.random())
    print(threading.current_thread().name, "is running....")

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=show, args=('thread-' + str(i),))
        t.start()
