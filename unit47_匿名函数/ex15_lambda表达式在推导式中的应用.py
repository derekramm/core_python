#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex15_lambda表达式在推导式中的应用.py"""


def func():
    fs = []
    for i in range(4):
        def lam(x=i):
            return i * i  # 变量x未被使用

        fs.append(lam)
    return fs


print(func()[0](1))  # 9
print(func()[1](1))  # 9
print(func()[2](1))  # 9
print(func()[3](1))  # 9
