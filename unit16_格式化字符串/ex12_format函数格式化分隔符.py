#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex12_format函数格式化分隔符.py"""

# [ [fill] align ] [sign] [#] [0] [width] [,] [.precision] [type]
# 可选，为数字添加分隔符，如：1,000,000

print(
    '{:,}'.format(333333333),  # 333,333,333
    '{}'.format(333333333),  # 333333333
    sep='\n'
)
