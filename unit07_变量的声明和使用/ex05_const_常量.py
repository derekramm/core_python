#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex05_const_常量.py
常量是运行过程数值不会发生变化的量，在python中不存在真正意义上的常量"""

import math

print(f'圆周率常量 = {math.pi}')
print(f'自然数常量 = {math.e}')

# 常量的值允许被修改
math.pi = 3.14
math.e = 2.71

print()
print('修改后的值：')
print(f'圆周率常量 = {math.pi}')
print(f'自然数常量 = {math.e}')
