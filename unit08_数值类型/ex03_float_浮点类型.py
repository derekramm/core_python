#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_float_浮点类型.py"""

# float:浮点型，就是我们说的小数
# 以下几种是我们常用的浮点类型

print(type(3.0))  # <class 'float'>
print(type(3.))  # 小数位不写，自动补0，也是浮点型<class 'float'>
print(type(3.14))
print(type(.14))  # 整数位缺失，默认为0.14
print(type(-3.14e6))  # 科学计数法也是浮点型
