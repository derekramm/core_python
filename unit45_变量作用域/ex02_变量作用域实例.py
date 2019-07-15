#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex02_变量作用域实例.py"""

x = 100


def func():
    print("func start:")
    x = 1000
    print("x=", x)
    x = x + 1
    print("x=", x)
    print("func end:")
    return


print(x)  # 100
func()
print(x)  # 100
