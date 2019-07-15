#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex10_列表insert函数.py"""

# 追加另一个列表: lst.insert(index, obj)

a = [1, 2, 9, 10, 3, 4, 8, 'a', 'a', 20, 30, 40]
b = a.insert(2, [100, 200])
print(b)
print(type(b))

a = [1, 2, [100, 200], 9, 10, 3, 4, 8, 'a', 'a', 20, 30, 40]
b = a.insert(2, 100)
print(a)
