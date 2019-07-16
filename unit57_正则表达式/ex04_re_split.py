#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_re_split.py"""

# re.split(pattern, string[, maxsplit=0, flags=0])
# 按照能够匹配的子串将string分割后返回列表

import re

s = '1,one,2,two,3,three'
m = re.split(',', s)
print(m)  # ['1', 'one', '2', 'two', '3', 'three']

