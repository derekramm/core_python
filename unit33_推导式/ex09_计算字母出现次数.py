#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex09_计算字母出现次数.py"""

message = 'hello xiaoming, my name is derek, nice to meet you'
d = {k: message.count(k) for k in {c for c in message}}
print(d)

items = list(d.items())

items.sort(key=lambda xm: xm[1], reverse=True)

print(items)
