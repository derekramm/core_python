#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex05_函数当作参数传参.py"""


def func(x, y, f):
    return f(x) + f(y)


def format(name):
    return name.capitalize()


print(func('xiao', 'ming', format))
