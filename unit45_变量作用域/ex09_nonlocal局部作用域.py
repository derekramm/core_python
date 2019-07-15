#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex09_nonlocal局部作用域.py"""


def func1():
    x = 100

    def func2():
        x = 200

    print(x)  # 100
    func2()
    print(x)  # 100


func1()


def func1():
    x = 100

    def func2():
        nonlocal x
        x = 200

    print(x)  # 100
    func2()
    print(x)  # 200


func1()
