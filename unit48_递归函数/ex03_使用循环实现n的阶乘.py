#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex03_使用循环实现n的阶乘.py"""


# 计算整数n的阶乘_使用循环实现

def fact(n):
    r = 1
    i = 1
    while i <= n:
        r *= i
        i += 1
    return r


a = fact(5)
print(a)  # 120
