#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_迭代器转换函数.py"""

from collections import Iterator

print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('xiaoming'), Iterator))
print(isinstance((x for x in range(18)), Iterator))
# print(isinstance(iter(18), Iterator))
