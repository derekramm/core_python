#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_列表逻辑运算.py"""

# 列表 and 运算

print([] and [1, 2, 3])
print([1, 2] and [])
print([1, 2] and ["aa"])

# 列表 or 运算

print([] or [1, 2])
print([1, 2] or [])
print([] or [])
print([1, 2] or [3, 4])

# 列表 not 运算

print(not [])
print(not [1, 2])
