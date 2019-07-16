#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_序列解包.py"""

# 序列解包-常规写法

names = ['小铭', '大蜥蜴']
xm = names[0]
dxy = names[1]
print(xm, dxy)

# 序列解包-优雅写法

names = ['小铭', '大蜥蜴']
xm, dxy = names
print(xm, dxy)
