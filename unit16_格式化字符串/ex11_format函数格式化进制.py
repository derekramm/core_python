#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex11_format函数格式化进制.py"""

# [ [fill] align ] [sign] [#] [0] [width] [,] [.precision] [type]
# 可选，对于二进制、八进制、十六进制，如果加上#，会显示 0b/0o/0x，否则不显示

print(
    '{:#b}'.format(333),  # 0b101001101
    '{:#o}'.format(333),  # 0o515
    '{:#d}'.format(333),  # 333
    '{:#x}'.format(333),  # 0x14d
    sep='\n'
)
