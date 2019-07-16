#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_加减法运算符重载.py"""

class MyNumber:
    def __init__(self, value):
        self.data = value
    def __repr__(self):
        return "MyNumber(%d)" % self.data
    def __add__(self, right):
        return MyNumber(self.data + right.data)
    def __sub__(self, right):
        return MyNumber(self.data - right.data)

n1 = MyNumber(100)
n2 = MyNumber(200)
print(n1 + n2)
print(n1 - n2)
