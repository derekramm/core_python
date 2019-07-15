#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_元组相关函数.py"""

a = (1, 2, 3)
print(a)
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(a)

reversed(a)

for n in reversed(a):
    print(n)
