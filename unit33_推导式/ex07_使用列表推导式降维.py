#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_使用列表推导式降维.py"""


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([i for r in matrix for i in r])
