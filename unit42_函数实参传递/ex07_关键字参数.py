#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_关键字参数.py"""

def get_fullname(firstname, lastname, middlename):
    print('{} {} {}'.format(firstname, middlename, lastname))

# 使用关键字参数时，实参顺序和形参顺序可以不一样
get_fullname(firstname='ramm', middlename='derek', lastname='dxy')

