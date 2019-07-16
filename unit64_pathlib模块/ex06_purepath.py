#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_purepath.py"""

from pathlib import *
print(PureWindowsPath('c:/program files/python3/site-packages/').drive)  # c:
print(PureWindowsPath('/program files/python3/site-packages/').drive)  # 空字符串
print(PurePosixPath('/usr/local/python3/bin/').drive)  # 空字符串

print(PureWindowsPath('c:/program files/python3/site-packages/').root)  # \
print(PureWindowsPath('/program files/python3/site-packages/').root)  # \
print(PurePosixPath('/usr/local/python3/bin/').root)  # /

print(PureWindowsPath('c:/program files/python3/site-packages/').anchor)  # c:\
print(PureWindowsPath('/program files/python3/site-packages/').anchor)  # \
print(PurePosixPath('/usr/local/python3/bin/').anchor)  # /
