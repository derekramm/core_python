#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex11_import函数.py"""

# __import__  函数根据给定的字符串名字，导入模块(动态导入)

# 语法

s = __import__('sys')
print(s)

m = __import__('math')
print(m.pi)
