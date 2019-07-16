#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex01_闭包访问限制.py"""


def line_config():
    def line(x):
        return 2 * x + 3

    print(line(5))


line_config()  # 13
print(line(5))  # NameError: name 'line' is not defined
