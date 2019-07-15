#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_创建集合示例.py"""

s = {1, 2, 3, 8, 2}
print(s)

s = {1, "abc", 0, (1, 2)}
print(s)

try:
    s = {1, [1, 2], 0, (1, 2)}
except Exception as ex:
    print(ex)

try:
    s = {1, {1:"2"}, "22"}
except Exception as ex:
    print(ex)
