#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex05_闭包实现计算器.py"""


def calculator(x):
    def calculate(y):
        return x * y

    return calculate


cal = calculator(0.8)

print(cal(10))  # 8
print(cal(100))  # 80
