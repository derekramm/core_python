#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_文件对象操作.py"""

# 读取一定大小的数据, 然后作为字符串或字节对象返回
# size是一个可选的数字类型的参数，用于指定读取的数据量
# 当size被忽略了或者为负值，那么该文件的所有内容都将被读取并且返回

f = open("readme.md", "r")

str = f.read(1024)
print(str)

f.close()
