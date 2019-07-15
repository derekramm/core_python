#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex02_返回多个数累加和.py"""


def add(num1, num2):
    return num1 + num2


print('{} + {} = {}'.format(12, 3, add(12, 3)))

# 有返回值的函数可以更加灵活的扩展需求
print('1 + 2 + 3 = {}'.format(add(add(1, 2), 3)))
