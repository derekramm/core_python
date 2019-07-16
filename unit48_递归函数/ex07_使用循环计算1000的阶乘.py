#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex07_使用循环计算1000的阶乘.py"""


# 使用循环计算1000的阶乘

def fact(n):
    r = 1
    i = 1
    while i <= n:
        r *= i
        i += 1
    return r


print(fact(1000))
