#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex16_匿名函数做返回值.py"""


# lambda 表达式产生的匿名函数可以做函数的返回值

def lam(x, y):
    return lambda: x * x + y * y


f = lam(2, 4)

print(f)  # <function lam.<locals>.<lambda> at 0x109d997b8>
print(f())  # 20
