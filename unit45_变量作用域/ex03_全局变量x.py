#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex03_全局变量x.py"""

x = 100


def func():
    a = x + 1
    print('a =', a)
    print('x =', x)
    return


func()
print(x)
