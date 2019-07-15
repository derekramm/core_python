#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_布尔转换对象.py"""

# 布尔类型中常用的False值
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(0.0j))
print(bool(''))
print(bool(()))
print(bool([]))
print(bool({}))

# 只要不为以上这些，大部分都是True
print(bool(1))
print(bool('xiaoming'))
print(bool([1, 2, 3, 4]))
