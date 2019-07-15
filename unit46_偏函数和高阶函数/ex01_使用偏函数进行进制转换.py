#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex01_使用偏函数进行进制转换.py"""

import functools

int2 = functools.partial(int, base=2)

print(int2('1000000'), int2('1010101'))

