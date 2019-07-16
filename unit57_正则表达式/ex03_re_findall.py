#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_re_findall.py"""

import re

# findall()
s = 'hello, python, world'
m = re.findall('o', s)
print(m)

# findtier()
s = '1, one, 2, two, 3, three'
m = re.finditer('\d+', s)
for _ in m:
    print(_)

