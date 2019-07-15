#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_序列解包.py"""

# 常规写法
info = ['java', 'man', 'python']
name = info[0]
sex = info[1]
tech = info[2]
print(name, sex, tech)

# 优雅写法
info = ['java', 'man', 'python']
name, sex, tech = info
print(name, sex, tech)
