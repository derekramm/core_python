#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex04_随机生成整数方法.py"""

import random

for _ in range(10):
    print(random.randrange(5), end=' ')

print()

for _ in range(10):
    print(random.randrange(3, 9, 2), end=' ')
