#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex10_默认参数.py"""

def count_money(price, count, discount=1.0):
    print(price * count * discount)

count_money(100, 10)  # discount 使用默认值
count_money(100, 10, 0.8)
