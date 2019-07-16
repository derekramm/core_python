#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_线程的作用.py"""

import threading
import time
import random

def add():
    sum_ = 0
    for i in range(1, 10000):
        sum_ += i
    print(sum_)

def mul():
    total = 1
    for i in range(1, 10000):
        total *= i
    print(total)

if __name__ == '__main__':
    start = time.perf_counter()
    add()
    mul()
    end = time.perf_counter()
    print(end - start)

    print('*' * 20)

    start = time.perf_counter()
    threading.Thread(target=add, ).start()
    threading.Thread(target=mul, ).start()
    end = time.perf_counter()
    print(end - start)
