#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_元组生成函数.py"""

t = tuple()
print(t)

t = tuple("abcdefg")
print(t)

t = tuple([1, 2, 3, 5])
print(t)

a = tuple(t)
print(a)

print(t is a)
