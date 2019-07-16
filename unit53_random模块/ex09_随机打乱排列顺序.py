#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex09_随机打乱排列顺序.py"""

import random

# 随机打乱序列x内元素的排列顺序
# 只能针对可变的序列

letters = [chr(n) for n in range(65, 91)]
print(letters)

random.shuffle(letters)
print(letters)
