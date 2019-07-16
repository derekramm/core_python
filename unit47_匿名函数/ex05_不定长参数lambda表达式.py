#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex05_不定长参数lambda表达式.py"""

func = lambda *args: sum(args)

print(func(1, 2, 3, 4))  # 10
