#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_remove.py"""

A = {1, 2, 3, 4, 5, 6, 'yy', (8, 1, 7), 17}
A.remove("yy")
print(A)

try:
    A.remove("zz")
except Exception as ex:
    print(ex)
