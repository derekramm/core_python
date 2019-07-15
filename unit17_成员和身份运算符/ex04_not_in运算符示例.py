#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_not_in运算符示例.py"""

animals = ["dog", "cat", "rabbit"]
an2 = 'snake'
print(an2 not in animals)  # an2不在列表中，返回 True
an2 = 'dog'
print(an2 not in animals)  # an2在列表中，返回 False
