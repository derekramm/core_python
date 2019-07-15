#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex14_列表切片删除元素.py"""

# 切片赋值可以删除列表元素

a = [1, 7, 'a', 'b', 8, 9, 10]
print(a)

a[1:6] = []
print(a)
