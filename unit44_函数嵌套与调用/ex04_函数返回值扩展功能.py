#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex04_函数返回值扩展功能.py"""

# 可以创建新函数，对函数返回值的进一步处理，用来扩展功能，比如：

import time


# 获取时间
def get_sys_time():
    return time.localtime()


# 格式化时间
def format_time(*time):
    return '{}年{}月{}日 {}时{}分{}秒'.format(*time)


# 输出时间
print(format_time(*get_sys_time()))
