#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex09_format函数格式化对齐.py"""

# [ [fill] align ] [sign] [#] [0] [width] [,] [.precision] [type]
# 可选，对齐方式（需配合width使用）
# <：内容左对齐
# >：内容右对齐(默认)
# ^：内容居中

print('{:0<16d}'.format(12))  # 1200000000000000
print('{:0>16d}'.format(12))  # 0000000000000012
print('{:0^16d}'.format(12))  # 0000000120000000
