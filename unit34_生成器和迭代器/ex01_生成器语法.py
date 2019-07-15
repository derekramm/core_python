#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_生成器语法.py"""

# 把一个列表推导式中的[]改成()，就创建了一个生成器

lst = [i for i in range(10)]
print(lst)

gtr = (i for i in range(10))
print(gtr)
