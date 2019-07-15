#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex09_多条件内容判断.py"""

# 多条件内容判断至少一个成立_常规方法

math, english, computer = 90, 80, 88
if math < 60 or english < 60 or computer < 60:
    print('not pass')

# 多条件内容判断至少一个成立_优雅方法

math, english, comp = 90, 59, 88
if any([math < 60, english < 60, comp < 60]):
    print('not pass')
