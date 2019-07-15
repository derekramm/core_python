#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex03_位置参数与不定长参数输出.py"""

def test_var_args(f_arg, *args):
    print('first normal arg:', f_arg)
    for arg in args:
        print('another arg through * args:', arg)


test_var_args('python', 'assert', 'not', 'and', 'or')