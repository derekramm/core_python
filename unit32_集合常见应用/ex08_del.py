#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_del.py"""

A = {(1, 3, 8)}
del A
try:
    print(A)
except Exception as ex:
    print(ex)

B = frozenset({1, 2, 3, 4})
del B
try:
    print(B)
except Exception as ex:
    print(ex)
