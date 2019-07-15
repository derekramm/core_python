#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_实现偶数累加.py"""

# 使用for循环实现10以内所有偶数的和，完成打印结果之后，提示计算已完成。

total = 0
for i in range(10):
    if i % 2 == 0: total, i = total + i, i + 1

print('计算已完成，结果为：', total)
