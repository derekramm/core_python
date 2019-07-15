#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_判断语句.py"""

# 判断语句_常规方法

x = -6
if x < 0:
    y = -x
else:
    y = x
print(y)

# 判断语句_优雅方法

x = -6
y = -x if x < 0 else x
print(y)
