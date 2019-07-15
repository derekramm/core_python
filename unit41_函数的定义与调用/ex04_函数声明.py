#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_函数声明.py"""

def my_func():
    print('this is my custom function')

def add():
    num1 = int(input('please enter a number: '))
    num2 = int(input('please enter another number: '))
    print('{} + {} = {}'.format(num1, num2, num1 + num2))

add()  # 调用（执行）add()函数
my_func()  # 调用（执行）my_func()函数
