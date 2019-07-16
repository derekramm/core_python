#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_re_compile.py"""

import re

cmp = re.compile('xm', re.I)
s = 'hello, xm! nice to meet you XM.'
m = re.findall(cmp, s)
print(m)