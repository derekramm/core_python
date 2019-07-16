#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex07_seq从非空序列随机选取一个元素.py"""

import random

# 从非空序列seq中随机选取一个元素，如果seq为空则弹出 IndexError异常

c = random.choice(range(9801, 9812))
print(c, chr(c))
