#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex07_闭包注意事项.py"""


# 2、声明Enclosing作用域变量后，就可以修改外部作用域的变量

def foo():
    name = ''

    def change_name():
        nonlocal name  # 声明Enclosing作用域变量后，就可以修改外部作用域的变量
        name = 'xiaoming'
        print('hello', name)

    change_name()
    print('hello', name)


foo()
