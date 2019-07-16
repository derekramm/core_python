#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex17_函数式编程中的lambda表达式.py"""

from functools import reduce

print(
    reduce(lambda a, b: a + b, range(10))
)

# 45
