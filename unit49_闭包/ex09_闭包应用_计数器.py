#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex09_闭包应用_计数器.py"""


# 计数器_v2.0_错误版 ❌

def counter():
    index = 0
    index += 1
    print(index)


for _ in range(3):
    counter()

# 1
# 1
# 1
