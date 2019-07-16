#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_文件对象操作_readlines.py"""

# 将文件中所有的行，一行一行全部读入一个列表内
# 按顺序一个一个作为列表的元素，并返回这个列表

f = open("readme.md", "r")
a = f.readlines()
print(a)
f.close()
