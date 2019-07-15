#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_使用for循环实现长度.py"""

msg = input('请输入消息：')

length = 0

for _ in msg:
    length += 1

print('消息的总长度为：', length)
