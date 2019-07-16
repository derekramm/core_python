#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_非空判断.py"""

# 非空判断-常规写法

A, B, C = [1, 3, 5], {}, ''
if len(A) > 0:
    print('A 为非空')
if len(B) > 0:
    print('B 为非空')
if len(C) > 0:
    print('C 为非空')

# 非空判断-优雅写法

A, B, C = [1, 3, 5], {}, ''
if A:
    print('A 为非空')
if B:
    print('B 为非空')
if C:
    print('C 为非空')
