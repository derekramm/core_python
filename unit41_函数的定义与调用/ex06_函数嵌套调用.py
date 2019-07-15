#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_函数嵌套调用.py"""


def get_fullname():
    return 'xiao' + 'ming'


def show_hello():
    print('hello', get_fullname())


show_hello()
