#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_re_sub.py"""

# re.sub(pattern, repl, string, count=0, flags=0)
# 使用re替换string中每一个匹配的子串后返回替换后的字符串

import re

s = '1, one, 2, two, 3, three'
m = re.sub(',', '-', s)
print(m)