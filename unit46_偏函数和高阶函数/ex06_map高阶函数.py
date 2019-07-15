#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex06_map高阶函数.py"""


# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f(x):
    return x ** 2


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))
