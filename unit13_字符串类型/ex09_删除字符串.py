#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex09_删除字符串.py"""

# 可以使用 del 删除一个字符串
# del str

s = '1234'
del s

try:
    print(s)
except Exception as ex:
    print(ex)
