#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex09_关键字参数示例02.py"""

def get_fullname(firstname, lastname, middlename):
    print('{} {} {}'.format(firstname, middlename, lastname))


# (**dict)：拆分字典中每一组键值对，对应传入
get_fullname(**dict(firstname='xiao', middlename='m', lastname='ing'))