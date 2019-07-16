#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex02_random_seed_生成相同随机数.py"""

import random

# 每次循环生成的随机数都相同

for _ in range(10):
    random.seed(a=10)
    print(random.random())
