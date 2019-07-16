#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex06_基本装饰器的语法.py"""

import time


def decorator(func):
    def decorate_method():
        print('begin decorate')
        func()
        print('after decorate')

    return decorate_method


@decorator
def show_time():
    print(time.asctime())


show_time()
