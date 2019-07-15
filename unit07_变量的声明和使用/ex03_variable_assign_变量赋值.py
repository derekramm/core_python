#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex03_variable_assign_变量赋值.py
变量赋值"""

# 单变量赋值
author = '达内'

# 多变量赋相同值
course = skill = 'Python'

# 多变量赋不同值
name, age = '小铭', 18

# 变量交换
course, skill = skill, course

# 函数作为值传递给新的变量
show = print

# 输出
show(author, course, skill, name, age)
