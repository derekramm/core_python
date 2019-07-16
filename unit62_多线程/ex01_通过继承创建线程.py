#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_通过继承创建线程.py"""

import threading
import time
import random

class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        time.sleep(random.random())
        print(threading.current_thread().name)

if __name__ == '__main__':
    for i in range(10):
        MyThread().start()