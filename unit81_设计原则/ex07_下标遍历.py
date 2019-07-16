#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_下标遍历.py"""

# 遍历下标-常规写法

L = ['小铭', '大蜥蜴']
for i in range(len(L)):
    print(i, ':', L[i])

# 遍历下标-优雅写法

L = ['小铭', '大蜥蜴']
for k, v in enumerate(L):
    print(k, ':', v)
