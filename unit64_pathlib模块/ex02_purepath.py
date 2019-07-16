#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_purepath.py"""

from pathlib import *
pp = PurePath()  # 如果不传入参数，默认使用当前路径
print(pp)  # .

# 传入的参数包含多个根路径，则只有最后一个根路径及后面的子路径生效
pp = PurePosixPath('/etc', '/usr', 'python3')
print(pp)  # /usr/python3

pp = PureWindowsPath('c:\windows', 'd:\program files', 'python3')
print(pp)  # d:\program files\python3
