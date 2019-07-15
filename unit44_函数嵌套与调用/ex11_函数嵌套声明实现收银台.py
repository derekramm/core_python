#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex11_函数嵌套声明实现收银台.py"""

def get_money(style, price, count):
    total = price * count  # 商品总价

    def by_return(t):
        return t - (t / 100) * 20

    def by_discount(t):
        return t * 0.6

    if style == 1:
        return by_return(total)
    elif style == 2:
        return by_discount(total)
    else:
        return total


print(get_money(1, 50., 10))
print(get_money(2, 50., 10))
print(get_money(3, 50., 10))
