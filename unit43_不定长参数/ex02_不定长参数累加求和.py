#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex02_不定长参数累加求和.py"""

def get_total(total, *nums):
    for n in nums:
        total += n
    print(total)


get_total(10, 1, 2, 3, 4)  # total = 20

get_total(0, *[1, 2, 3, 4])  # 调用时，不定长参数必须放置在后面
