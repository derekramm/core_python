#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_文件对象操作_tell.py"""

f = open("about.txt", "rb+")
f.write(b"abcdefghijklmnopqrstuvwxyz")

print(f.tell())  # 26

f.seek(5)
print(f.read(1))  # f

f.seek(-3, 2)
print(f.read(1))  # x