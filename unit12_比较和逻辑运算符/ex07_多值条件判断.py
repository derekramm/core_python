#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_多值条件判断.py"""

# 多值符合条件判断_常规方法

num = 1
if num == 1 or num == 3 or num == 5:
    type = '奇数'
print(type)

# 多值符合条件判断_优雅方法

num = 1
if num in (1, 3, 5):
    type = '奇数'
print(type)
