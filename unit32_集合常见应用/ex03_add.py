#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_add.py"""

A = {1, 2, 3, 4, 5, 6}
A.add(17)
print(A)
A.add("yy")
print(A)

s3 = {8, 1, 7}
A.add(tuple(s3))
print(A)
