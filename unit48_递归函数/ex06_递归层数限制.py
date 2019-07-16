#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex06_递归层数限制.py"""


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(30))
# 265252859812191058636308480000000

print(fact(1000))
# RecursionError: maximum recursion depth exceeded in comparison
