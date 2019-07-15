#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_混合类型集合操作.py"""

A = {1, 2, 3}
B = frozenset({1, 2, 3, 4})
print(A | B)
print(B | A)

print(A ^ B)

print(B ^ A)

print(A - B)
print(B - A)
