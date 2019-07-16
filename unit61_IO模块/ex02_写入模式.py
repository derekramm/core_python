#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_写入模式.py"""

s = 'hello, xiaoming'
b = bytes(s, encoding='utf-8')

f = open('about.txt', 'w')
f.write(s)