#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex05_第三方模块.py"""

# pip install xpinyin
from xpinyin import Pinyin

p = Pinyin()
print(p.get_pinyin("北京"))  # bei-jing
