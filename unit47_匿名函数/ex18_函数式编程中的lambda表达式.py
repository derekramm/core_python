#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex18_函数式编程中的lambda表达式.py"""

# lambda表达式是起到一个函数速写的作用，允许在代码内嵌入一个函数的定义

print(
    list(
        filter(
            lambda x: True if x % 3 == 0 else False, range(10)
        )
    )
)

# [0, 3, 6, 9]
