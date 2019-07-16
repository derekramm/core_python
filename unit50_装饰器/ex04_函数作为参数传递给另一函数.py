#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex04_函数作为参数传递给另一函数.py"""


def hi():
    return 'hi '


def after_hi(func, name):
    return func() + name


print(after_hi(hi, 'xiaoming'))  # hi xiaoming
