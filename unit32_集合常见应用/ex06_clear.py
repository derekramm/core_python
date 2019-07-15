#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_clear.py"""

A = {2, 3, 4, 5, 6, (8, 1, 7)}
A.clear()
print(A)

B = frozenset({1, 2, 3, 4})

try:
    B.clear()
except Exception as ex:
    print(ex)
