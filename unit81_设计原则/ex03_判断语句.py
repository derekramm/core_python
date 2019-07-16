#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_判断语句.py"""

# 判断语句-常规写法

x = -6
if x < 0:
    y = -x
else:
    y = x
print(y)

# 判断语句-优雅写法

x = -6
y = -x if x < 0 else x
print(y)
