#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex04_闭包.py"""


def line_config(a, b):
    def line(x):
        return a * x + b

    return line


line = line_config(2, 3)
print(line(5))  # 13
print(line.__closure__)
print(line.__closure__[0].cell_contents)
print(line.__closure__[1].cell_contents)
