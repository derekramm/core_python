#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_创建不可变集合.py"""

s = frozenset()
print(s)
print(type(s))

s = frozenset("abcd")
print(s)

s = frozenset((1, 2, 8, 4))
print(s)

s = frozenset([1, 2, 5])
print(s)

d = {1: 'yy', 2: 'zz'}
s = frozenset(d)
print(s)
