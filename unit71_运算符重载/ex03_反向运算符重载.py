#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_反向运算符重载.py"""

class MyNumber:
    def __add__(self, rhs):
        pass

n1 = MyNumber()
print(n1 + 10)  # 正确

print(10 + n1)  # TypeError