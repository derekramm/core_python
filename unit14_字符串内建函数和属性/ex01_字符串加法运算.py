#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_字符串加法运算.py"""

name = 'xiao' + 'ming'
name1 = name + name
print(name1)  # xiaomingxiaoming

name += '大蜥蜴'
print(name)  # xiaoming大蜥蜴

# 注意：通过 += 符号赋值后，字符串将创建新的空间地址
user_name = 'xiao'
print(id(user_name))

user_name += 'ming'
print(id(user_name))
