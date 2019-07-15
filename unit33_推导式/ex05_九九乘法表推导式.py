#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_九九乘法表推导式.py"""

multi_table = [(j, i, i * j) for i in range(1, 10) for j in range(1, i + 1)]
print(multi_table)
