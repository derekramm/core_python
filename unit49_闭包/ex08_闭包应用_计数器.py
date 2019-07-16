#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex08_闭包应用_计数器.py"""

# 计数器_v1.0

index = 0


def counter():
    global index
    index += 1


for _ in range(3):
    counter()
    print(index)
