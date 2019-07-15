#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_判断是否是迭代器.py"""

from collections import Iterator

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('xiaoming', Iterator))
print(isinstance((x for x in range(18)), Iterator))
print(isinstance(18, Iterator))
