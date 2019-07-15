#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex01_lambda表达式示例.py"""


# 传统定义函数

def func(x):
    return x * x


a = func(2)
print(a)

# 使用lambda表达式

f = lambda x: x * x
a = f(2)

print(a)
