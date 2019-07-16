#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_re_match.py"""

import re

s = 'hello, xiaoming'
m = re.match('hello(, )(.*)', s)
print(m)
print(m.span())
print(m.group())
print(m.group(1))
print(m.group(2))



