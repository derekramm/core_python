#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex01_不使用递归函数的实现.py"""

index = 1


def foo():
    global index
    if index <= 3:
        print(index)
        index += 1


# 不使用递归时，需要重复调用函数
foo()  # 1
foo()  # 2
foo()  # 3
