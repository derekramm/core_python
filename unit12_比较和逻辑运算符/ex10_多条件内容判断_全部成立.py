#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex10_多条件内容判断_全部成立.py"""

# 多条件内容判断全部成立_常规方法

math, English, computer = 90, 80, 88
if math > 60 and English > 60 and computer > 60:
    print('pass')

# 多条件内容判断全部成立_优雅方法

math, English, computer = 90, 80, 88
# 使用 all() 函数判断时，要求所有条件必须全部成立
if all([math > 60, English > 60, computer > 60]):
    print('pass')
