#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_布尔运算.py"""

print(True == 1)  # True
print(False == 0)  # False
print(True + 1)  # 2
print(False + 1)  # 1
print(False - True)  # -1
print(True + False)  # 1

# 通过 isinstance()函数可以帮助我们判断一个类型是否是另一个类型的子类
# 如果是的话，返回True，不是返回False
print(isinstance(True, int))  # True
