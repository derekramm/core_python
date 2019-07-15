#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_is运算符.py"""

age1 = 18
age2 = 18

print(age1 is age2)

salary1 = 18000
salary2 = 18000
print(salary1 is salary2)

# 注意
# Python仅仅对比较小的整数对象进行缓存（范围为 [-5, 256] ），而非是所有整数
# 另外，在脚本文件或者IDE环境下，因为优化可能会看不到效果
