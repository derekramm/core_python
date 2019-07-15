#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_参数的概念.py"""

def show_hello(name):  # 定义参数时用到的叫形参
    print('hello', name)

show_hello('xiaoming')  # 调用参数时用到的叫实参

def add(num1, num2):  # 函数定义时允许有多个形参
    print('{} + {} = {}'.format(num1, num2, num1 + num2))

add(12, 3)  # 调用时实参需要和形参对应
