#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex05_基本装饰器的概念.py"""

import time


def decorator(func):
    def decorate_method():
        print('begin decorate')
        func()
        print('after decorate')

    return decorate_method


def show_time():
    print(time.asctime())


decorator(show_time)()
