#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex01_random_seed_生成不同随机数.py"""

import random

# 每次循环生成不同的随机数，但是下次执行时，依然是相同的三个结果

random.seed(a=10)
for _ in range(10):
    print(random.random())
