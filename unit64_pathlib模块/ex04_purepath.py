#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_purepath.py"""

from pathlib import *
pp_xm = PurePosixPath('xm')
pp_dxy = PurePosixPath('dxy')

print(pp_xm / 'python' / 'lesson_01')  # xm/python/lesson_01
print(pp_xm / pp_dxy)  # xm/dxy
