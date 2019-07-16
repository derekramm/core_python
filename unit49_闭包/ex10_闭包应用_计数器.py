#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex10_闭包应用_计数器.py"""


# 计数器_v3.0

def counter():
    index = 0

    def add_index():
        nonlocal index
        index += 1
        print(index)

    return add_index


c = counter()
print(c)

for _ in range(3):
    c()
