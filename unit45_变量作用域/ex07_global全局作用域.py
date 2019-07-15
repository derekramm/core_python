#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex07_global全局作用域.py"""

x = 99


def func():
    x = 100


print(x)  # 99
func()
print(x)  # 99

x = 99


def func():
    global x  # 声明x为全局变量
    x = 100


print(x)  # 99
func()
print(x)  # 100
