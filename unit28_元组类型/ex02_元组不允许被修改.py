#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_元组不允许被修改.py"""

t = (1, 'yy', 2)
try:
    t[0] = 3
except Exception as ex:
    print(ex)  # 'tuple' object does not support item assignment

