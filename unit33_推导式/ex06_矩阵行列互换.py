#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_矩阵行列互换.py"""

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

rev_matrix = [[r[i] for r in matrix] for i in range(4)]
print(rev_matrix)
