#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex01_第一个函数.py"""


def hi(name):
    return 'hi' + name


print(hi('xiaoming'))  # hixiaoming

greet = hi
welcome = hi
print(greet('leguan'))  # hileguan
print(welcome('tuatara'))  # hituatara
