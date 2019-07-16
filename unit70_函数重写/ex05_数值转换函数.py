#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_数值转换函数.py"""

class MyNumber:
    def __init__(self, value):
        self.data = value
    def __int__(self):
        return int(self.data)
    def __float__(self):
        return float(self.data)
    def __bool__(self):
        return bool(int(self.data))

n1 = MyNumber('100')
print(int(n1))
print(float(n1))
print(complex(n1))
print(bool(n1))
