#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex10_通过切片获取新列表.py"""

# 通过切片获取新列表

a = [1, 2, 3, 4]
b = a[1:3]
c = a[:]  # 复制列表

print(a)
print(b)
print(c)
print(id(a), id(c))
