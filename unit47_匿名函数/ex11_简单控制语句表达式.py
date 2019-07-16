#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex11_简单控制语句表达式.py"""

func = lambda num: '成年' if num >= 18 else '未成年'

print(func(16))  # 未成年
print(func(18))  # 成年
