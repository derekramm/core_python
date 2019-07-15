#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_copy.py"""

# copy 方法,  得到字典副本

d = {'name': 'dxy', 'age': 18, 'height': 172, 'dxy': 19}
a = d.copy()
print(a)

print(a is d)
print(a == d)
