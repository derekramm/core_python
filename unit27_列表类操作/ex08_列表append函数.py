#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_列表append函数.py"""

# 向列表中添加元素: lst.append(obj)

a = [1, 2, 5, 6, 10, 4, 9, 9, 'aa']
b = a.append(10)
print(a)
print(b, type(b))

a.append([100, 200])
print(a)
