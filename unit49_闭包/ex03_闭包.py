#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex03_闭包.py"""


def line_config(a, b):
    def line(x):
        return a * x + b

    return line


line = line_config(2, 3)
print(line(5))  # 13
