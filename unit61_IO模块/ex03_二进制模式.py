#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_二进制模式.py"""

s = 'hello, world'
b = bytes(s, encoding='utf-8')

f = open('about.txt','wb')
f.write(b)
