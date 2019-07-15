#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex09_列表extend函数.py"""

# 插入元素: L.extend(iterable)

a = [1, 2, 9, 10, 3, 4, 8]
a.extend("aa")
print(a)

a.extend([100])
print(a)

a.extend([20, 30, 40])
print(a)
