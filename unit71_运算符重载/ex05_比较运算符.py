#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_比较运算符.py"""

class MyNumber:
    def __init__(self, value):
        self.data = value
    def __lt__(self, rhs):
        print("__lt__ is called")
        return self.data < rhs.data
    def __gt__(self, rhs):
        print("__gt__ is called")
        return self.data > rhs.data

n1 = MyNumber(100)
n2 = MyNumber(200)
print(n1 < n2)
print(n1 > n2)
