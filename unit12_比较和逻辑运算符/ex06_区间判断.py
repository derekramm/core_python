#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_区间判断.py"""

# 区间判断_常规方法

score = 82
if score >= 80 and score < 90:
    level = 'B'
print(level)

# 区间判断_优雅方法

score = 82
if 80 <= score < 90:
    level = 'B'
print(level)
