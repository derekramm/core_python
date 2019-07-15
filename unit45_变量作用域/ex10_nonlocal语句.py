#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex10_nonlocal语句.py"""


# 当外部没有定义x变量时，则会报错

def func1():
    nonlocal x  # SyntaxError: no binding for nonlocal 'x' found


def func1():
    def func2():
        nonlocal x  # SyntaxError: no binding for nonlocal 'x' found
