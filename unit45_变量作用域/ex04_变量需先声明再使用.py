#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex04_变量需先声明再使用.py"""


# func 函数内部对x赋值，确定为x为局部变量
# x = x +1，没有创建x时，就使用了x，所以报错

x = 100


def func():
    x = x + 1
    print(' x =', x)
    return


func()

# UnboundLocalError: local variable 'x' referenced before assignment
