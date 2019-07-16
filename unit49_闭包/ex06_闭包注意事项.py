#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex06_闭包注意事项.py"""


# 1、内部函数无法修改外部作用域的变量

def foo():
    name = ''

    def change_name():
        name = 'xiaoming'
        print('hello', name)

    change_name()
    print('hello', name)  # 内部函数无法修改外部作用域的变量


foo()
