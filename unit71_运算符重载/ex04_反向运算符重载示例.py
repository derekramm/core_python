#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_反向运算符重载示例.py"""

class MyNumber:
    def __init__(self, value):
        self.data = value
    def __repr__(self):
        return "MyNumber(%d)" % self.data
    def __add__(self, rhs):
        if type(rhs) is MyNumber:
            return MyNumber(self.data + rhs.data)
        elif type(rhs) is int:
            return MyNumber(self.data + rhs)
    def __radd__(self, lhs):
        return self + lhs

n1 = MyNumber(100)
print(n1 + 10)
print(20 + n1)  # 正常运行不会出错
