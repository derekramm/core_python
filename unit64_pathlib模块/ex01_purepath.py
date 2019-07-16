#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_purepath.py"""

from pathlib import *

pp = PurePath('index.py')
print(type(pp))  # <class 'pathlib.PurePosixPath'>

pp = PurePath('tedu', 'tlv', 'info')
print(pp)  # tedu/tlv/info

pp = PureWindowsPath(Path('tedu'), Path('tlv'), Path('info'))
print(pp)  # tedu\tlv\info
