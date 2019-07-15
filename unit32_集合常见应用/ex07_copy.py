#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_copy.py"""

A = {2, 3, 4, 5, 6, (8, 1, 7)}
b = A.copy()
print(b)

print(b == A)
print(b is A)

B = frozenset({1, 2, 3, 4})
c = B.copy()
print(c)
