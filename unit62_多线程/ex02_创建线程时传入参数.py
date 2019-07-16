#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_创建线程时传入参数.py"""

import threading
import time
import random

class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__(name=name)

    def run(self):
        time.sleep(random.random())
        print(threading.current_thread().name, 'is running...')

if __name__ == '__main__':
    for i in range(10):
        MyThread('thread-' + str(i)).start()