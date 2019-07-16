#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_purepath.py"""

from pathlib import *
pp_xm = PurePosixPath('xm', 'python', 'lesson_01')
pp_dxy = PureWindowsPath('dxy', 'python3', 'lesson_02')

print(type(pp_xm), pp_xm)
print(type(pp_dxy), str(pp_dxy))
