#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_list运算符重载.py"""

L1 = [1, 2, 3]
L2 = [4, 5, 6]

print(L1 + L2)  # [1, 2, 3, 4, 5, 6]
print(L1.__add__(L2))  # [1, 2, 3, 4, 5, 6]

print(L1 * 2)  # 等同于 L1.__mul__(2)
print(L1.__mul__(2))
