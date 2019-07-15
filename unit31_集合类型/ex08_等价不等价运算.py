#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_等价不等价运算.py"""

s1 = {1, 2, 3}
s2 = set((1, 2, 3))
print(s1 == s2)
print(s1 != s2)
print(s1 is s2)

s3 = frozenset((1, 2, 3))
print(s3 == s2)
print(s3 == s1)
