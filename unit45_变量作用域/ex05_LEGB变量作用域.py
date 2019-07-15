#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex05_LEGB变量作用域.py"""

# x 全局变量
# y 本地/局部变量
# z 本地/局部变量

x = 99  # 全局变量


def func(y):
    z = x + y  # 局部变量
    return z


print(func(1))  # 100
