#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex06_LEGB变量作用域.py"""

a = 100  # 全局变量（G）


def func1():
    a = 1  # 上级结构的局部变量（E）

    def func2():
        b = 2  # 局部变量
        print(a + b)

    print(a)
    func2()


print(a)  # 100
func1()  # 1 3
func2()  # 报错  NameError: name 'func2' is not defined
