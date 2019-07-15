#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex06_print_customize_自定义输出.py
自定义输出"""

import sys

# 自定义输出使用print函数完整参数列表
# 可以自定义每个数据的分隔符以及结束符号
print('hello', 'world', sep=', ', end='!\n', file=sys.stdout)
print('salute', 'Guido van Rossum', sep=' ', end='.', file=sys.stdout)
