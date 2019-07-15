#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_pop.py"""

A = {1, 2, 3, 4, 5, 6, (8, 1, 7)}
b = A.pop()
print(b)

C = set()
try:
    b = C.pop()
except Exception as ex:
    print(ex)
