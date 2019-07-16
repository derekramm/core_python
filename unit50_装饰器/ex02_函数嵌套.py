#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex02_函数嵌套.py"""


def hi(name):
    def greet():
        return 'greet ' + name

    def welcome():
        return 'welcome ' + name

    print(greet())  # greet xiaoming
    print(welcome())  # welcome xiaoming


hi('xiaoming')
