#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex02_闭包.py"""


def line_config():
    def line(x):
        return 2 * x + 3

    return line


line = line_config()
print(line(5))  # 13
