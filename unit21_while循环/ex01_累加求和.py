#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_累加求和.py"""

# 计算100以内所有正整数的和
# 当计算完成后，输出结果并输出 “计算已结束，请注意查看”。

index, total = 1, 0
while index <= 100:
    total += index
    index += 1
print(total)
