#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_通过主键查询.py"""

d2 = {'xm': 1234567, 'dxy': {'mob': '2345678', 'addr': '北京'}}
print(d2['xm'])

try:
    print(d2['age'])
except Exception as ex:
    print(ex)



