#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex03_变量名指向函数.py"""

print(abs(-10))  # 10
print(abs)  # <built-in function abs>

my_abs = abs

print(my_abs(-18))  # 18
