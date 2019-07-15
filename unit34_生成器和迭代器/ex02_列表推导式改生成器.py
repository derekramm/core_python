#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_列表推导式改生成器.py"""

# 把一个列表推导式中的[]改成()，就创建了一个生成器

g = (i for i in range(10))

for n in g:
    print(n, end=' ')
