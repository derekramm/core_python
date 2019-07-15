#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_in运算符示例.py"""

animals = ["dog", "cat", "rabbit"]
an1 = 'dog'
print(an1 in animals)  # an1在列表中，返回 True
an1 = 'snake'
print(an1 in animals)  # an1不在列表中，返回 False
