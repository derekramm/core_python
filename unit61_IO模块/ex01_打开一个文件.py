#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_打开一个文件.py"""

# 打开一个文件
f = open('readme.md', 'r')
content = f.read()

# 关闭打开的文件
f.close()
print(content)