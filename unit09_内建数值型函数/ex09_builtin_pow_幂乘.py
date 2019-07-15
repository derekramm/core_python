#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex09_builtin_pow_幂乘.py
内建函数：幂乘"""

import math

print(f'2的3次方是 {pow(2, 3)}')
print(f'5的5次方是 {pow(5, 5)}')

print()
r = int(input('请输入球体的半径：'))
print(f'球体体积为：{(4 / 3) * math.pi * pow(r, 3)}')
