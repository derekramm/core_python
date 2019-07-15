#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_元组定义.py"""

# 元组是不可改变的序列, 元组可以存放任意的值
# 元组语法: (元素,  ...)

print((1, 2, 3))  # 元组

t = ()  # 空元组
print(t)

t = (1, 'yy', 22)
print(t)

t = (1, 'yy', (2, 3, 4), 22)
print(t)
