#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_判断是否可迭代.py"""

from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('xiaoming', Iterable))
print(isinstance((x for x in range(18)), Iterable))
print(isinstance(18, Iterable))  # False
