#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex13_format函数格式化小数点精度.py"""

# [ [fill] align ] [sign] [#] [0] [width] [,] [.precision] [type]
# 可选，小数位保留精度

print(
    '{:.2f}'.format(3.1415926),  # 3.14
    sep='\n'
)
