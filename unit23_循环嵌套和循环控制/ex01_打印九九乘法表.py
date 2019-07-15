#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_打印九九乘法表.py"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={j * i}', end=' ')
    print()
