#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_元组的常用方法.py"""

# T.count(value)
# T.index(value, [start, [stop]])

a = (1, 2, 3, 2)
print(a.count(3))
print(a.count(2))
print(a.index(2))
print(a.index(3))
