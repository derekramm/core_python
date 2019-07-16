#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex07_带参数的装饰器的语法.py"""


def getparam(msg):
    def decorator(func):
        def decorate_method():
            print(msg)
            print('begin decorate')
            func()
            print('after decorate')

        return decorate_method

    return decorator


@getparam('extra info')
def show():
    print('hello')


show()
