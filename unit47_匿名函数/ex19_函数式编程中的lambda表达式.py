#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex19_函数式编程中的lambda表达式.py"""


def get_y(a, b):
    return lambda x: a * x + b


result = get_y(1, 1)

print(result(2))  # 3
