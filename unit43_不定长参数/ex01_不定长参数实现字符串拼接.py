#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex01_不定长参数实现字符串拼接.py"""

def show_hello(*names):
    for name in names:
        print('hello', name)


show_hello('xiao', 'ming', 'ramm', 'derek')

show_hello(('xiao', 'ming', 'ramm', 'derek'))
# hello ('xiao', 'ming', 'ramm', 'derek')

