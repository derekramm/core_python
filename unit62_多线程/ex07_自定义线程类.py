#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_自定义线程类.py"""

import threading
import time
import random

class MyThread(threading.Thread):
    def __init__(self, func, arg):
        super(MyThread, self).__init__()
        self.func = func
        self.arg = arg
    def run(self):
        time.sleep(random.random())
        self.func(self.arg)

def my_func(args):
    print(args)

if __name__ == '__main__':
    for i in range(10):
        obj = MyThread(my_func, 'thread-' + str(i))
        obj.start()
