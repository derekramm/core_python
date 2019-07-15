#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex08_reduce高阶函数.py"""

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))
