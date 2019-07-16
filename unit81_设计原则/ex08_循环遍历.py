#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_循环遍历.py"""

# 循环语句-常规写法

L = []
for i in range(1, 6):
    L.append(i * i)
print(L)

# 循环语句-优雅写法

print([x * x for x in range(1, 6)])
