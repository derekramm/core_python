#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex08_global语句.py"""


def func():
    global y
    y = 100


print(y)  # 报错，因为y没有被定义
func()
print(y)


def func():
    global z
    return


print(z)  # 报错
