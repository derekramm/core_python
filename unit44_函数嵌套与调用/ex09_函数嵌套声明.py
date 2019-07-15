#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex09_函数嵌套声明.py"""

# 除了在函数中调用其它函数之外，Python允许在函数中再定义函数。

# 例如：

def outer_func():
    print('this is from outer function')

    def inner_func():
        print('this is from inner function')

    inner_func()


outer_func()
