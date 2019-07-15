#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex13_列表插入元素.py"""

# 切片赋值可以不替换任何元素的情况下，为列表插入新元素

a = [1, 7, 8, 9, 10]
print(a)

a[2:2] = ['a', 'b']
print(a)
