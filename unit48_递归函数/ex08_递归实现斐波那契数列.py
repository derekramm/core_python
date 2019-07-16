#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex08_递归实现斐波那契数列.py"""


# 斐波那契数列

def foo(n):
    if n == 1 or n == 2:
        return 1
    return foo(n - 1) + foo(n - 2)


print(foo(30))  # 832040
