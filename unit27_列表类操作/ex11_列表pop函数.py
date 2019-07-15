#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex11_列表pop函数.py"""

# 删除并返回元素: lst.pop([index])

a = [2, 100, [100, 200], 9, 10, 3, 4, 8, 'a', 'a', 20, 30, 'c', 40]
b = a.pop()
print(a)
print(b)

c = a.pop(0)
print(a)
print(c)

d = a.pop(-1)
print(a)
print(d)
