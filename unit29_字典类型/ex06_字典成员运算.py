#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_字典成员运算.py"""

d2 = {'xm': 1234567, 'dxy': {'mob': '2345678', 'addr': '北京'}}

print('mob' in d2)  # False
print('mob' in d2['dxy'])  # True
print('age' in d2)  # False
