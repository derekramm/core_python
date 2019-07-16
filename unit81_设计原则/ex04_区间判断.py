#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_区间判断.py"""

# 区间判断-常规写法

score = 82
if score >= 80 and score < 90:
    level = 'B'
print(level)

# 区间判断-优雅写法

score = 82
if 80 <= score < 90:
    level = 'B'
print(level)
