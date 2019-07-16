#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_线程执行各自任务.py"""

# 在多线程执行过程中，有一个特点要注意，那就是每个线程各执行各的任务，不等待其它的线程
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
    time.sleep(random.random())
    print(threading.main_thread().name, 'is finished')