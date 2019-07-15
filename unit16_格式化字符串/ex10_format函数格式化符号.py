#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex10_format函数格式化符号.py"""

# [ [fill] align ] [sign] [#] [0] [width] [,] [.precision] [type]
# 可选，有无符号数字

print('{:*<+10}'.format(12),  # +12*******
      '{:*>-10}'.format(-12),  # *******-12
      '{:*^ 10}'.format(12),  # ****12****
      sep='\n')
