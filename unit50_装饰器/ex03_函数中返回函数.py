#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex03_函数中返回函数.py"""


def hi(name):
    def greet():
        return 'greet ' + name

    def welcome():
        return 'welcome ' + name

    return greet if name == 'xiaoming' else welcome


greet = hi('xiaoming')
welcome = hi('leguan')

print(greet())  # greet xiaoming
print(welcome())  # welcome leguan
