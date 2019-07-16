#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex04_关键字参数lambda表达式.py"""

func = lambda a=12, b=3: a + b

print(func())  # 15
print(func(b=18))  # 30
