#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex02_使用递归函数的实现.py"""

index = 1


def foo():
    global index
    if index <= 3:
        print(index)
        index += 1
        foo()  # 使用递归时，可以在满足条件的时候调用自身，重复执行


foo()
