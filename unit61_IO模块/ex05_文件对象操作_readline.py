#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_文件对象操作_readline.py"""


# 从文件中读取一行n内容,换行符为'\n'
# 如果返回一个空字符串，说明已经已经读取到最后一行
# 这种方法，通常是读一行，处理一行，并且不能回头，只能前进，读过的行不能再读了

f = open("readme.md", "r")
str = f.readline()
print(str)
f.close()