#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex11_遍历集合.py"""

A = {1, 2, 3}
for i in A:
    print(i)

B = frozenset(('a', 'b', 'c'))
print(B)
for c in B:
    print(c)
