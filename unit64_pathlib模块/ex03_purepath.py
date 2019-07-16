#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_purepath.py"""

from pathlib import *
# 在 Windows 风格的路径中，只有盘符才能算根路径，仅有斜杠是不算的
pp = PureWindowsPath('c:\windows', '\program files')
print(pp)  # c:\program files

# 传入的路径字相串中包含多余的来|杠和点号，系统会直接忽略它们
pp = PurePath('foo//bar')
print(pp)  # foo/bar
pp = PurePath('foo/./bar')
print(pp)  # foo/bar
