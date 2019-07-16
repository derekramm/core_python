#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex10_pure.py"""

from pathlib import *
p = Path('.')  # 获取当前目录

# 遍历当前目录下所有文件和子目录
for x in p.iterdir():
    print(x)

# 遍历所有py后缀的文件
for py in p.glob('*.py'):
    print(py)
