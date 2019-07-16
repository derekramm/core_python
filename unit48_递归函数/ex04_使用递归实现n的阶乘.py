#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex04_使用递归实现n的阶乘.py"""


# 计算整数n的阶乘
# 使用递归实现
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


a = fact(5)
print(a)
