#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex11_内部函数外部访问受限.py"""

# 这里需要注意的是，不要在外部函数和内部函数之间相互调用
# 否则会引发死循环的问题

def outer_func():
    print('this is from outer function')

    def inner_func():
        outer_func()
        print('this is from inner function')

    inner_func()


outer_func()
