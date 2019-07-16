#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_purepath.py"""

from pathlib import *
pp = PurePath('/usr/local/python3/bin/')
print(pp.parents[0])  # /usr/local/python3
print(pp.parents[1])  # /usr/local
print(pp.parents[2])  # /usr
print(pp.parents[3])  # /

print(pp.parent)  # /usr/local/python3
