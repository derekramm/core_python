#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex10_从样本随机抽取k个不重复元素.py"""

import random

# 从population样本或集合中随机抽取K个不重复的元素形成新的序列
# 常用于不重复的随机抽样，返回的是一个新的序列，不会破坏原有序列


numbers = random.sample(range(10000000), k=60)
print(numbers)
