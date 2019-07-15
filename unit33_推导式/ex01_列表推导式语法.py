#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_列表推导式语法.py"""

y = [x ** 2 for x in range(1, 10)]
print(y)

z = [x ** 2 for x in range(1, 10) if x % 2 == 1]
print(z)
