#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex03_return语句的返回值.py"""

def with_return_none():  # return 后面没有数据，表示该函数返回 None
    return


def without_return():  # 函数没有 return，表示该函数返回 None
    pass


def with_return_info():  # return 后面有数据，表示该函数有返回值
    return 'info'


print(with_return_none())  # None
print(without_return())  # None
print(with_return_info())  # info
