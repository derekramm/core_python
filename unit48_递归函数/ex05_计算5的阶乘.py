#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex05_计算5的阶乘.py"""


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


a = fact(5)
print(a)
