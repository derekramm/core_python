#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_多值判断.py"""

# 多值判断-常规写法

num = 1
if num == 1 or num == 3 or num == 5:
    type = '奇数'
print(type)

# 多值判断-优雅写法

num = 1
if num in (1, 3, 5):
    type = '奇数'
print(type)
