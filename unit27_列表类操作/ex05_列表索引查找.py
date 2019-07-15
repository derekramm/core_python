#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_列表索引查找.py"""

# 索引查找
# lst.index(value [, begin[, end]])

a = [1, 2, 5, 6, 10, 4, 9, 9]

print(a.index(9))
print(a.index(9, 7, 8))
print(a.index(9, 7, 19))
print(a.index(9, 7, ))
print(a.index(9, 7))
