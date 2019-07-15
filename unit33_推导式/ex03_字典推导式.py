#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_字典推导式.py"""

e = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(e)
e = {x: x ** 2 for x in [1, 2, 3, 4]}
print(e)
e = {x: x ** 2 for x in [1, 2, 3, 4] if x % 2 != 0}
print(e)
