#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex08_随机选取k个元素.py"""

import random

print(random.choices(['red', 'black', 'green'], [18, 18, 2], k=6))

# 3.6版本新增
# 从population集群中随机抽取K个元素
# weights是相对权重列表，cum_weights是累计权重，两个参数不能同时存在
