#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_打印10以内的偶数.py"""

# 打印出10以内的偶数
for num in range(10):
    # 跳过奇数
    if num % 2 == 1:
        continue
    # 打印偶数
    print(num)
