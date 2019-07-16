#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex11_随机生成0-1之间的浮点数.py"""


import random

# 返回一个介于左闭右开[0.0, 1.0)区间的浮点数
print(random.random())

# 返回一个介于a和b之间的浮点数
# 如果a>b，则是b到a之间的浮点数。这里的a和b都有可能出现在结果中
print(random.uniform(1, 10))
