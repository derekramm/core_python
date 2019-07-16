#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_re_search.py"""

import re

s = 'hello, xiaoming! nice to meet you'
m = re.search('(.*)(xiaoming)(.*)', s)
print(m)
print(m.span())
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.group(3))