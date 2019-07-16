#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_对象转字符串函数重写.py"""

class MyNumber:
    def __init__(self, value):
        self.data = value
    def __repr__(self):
        '''转换为eval能够识别的字符串'''
        return "MyNumber(%d)" % self.data
    def __str__(self):
        '''转换为普通字符串，用于显示给人看'''
        return "%d" % self.data

n1 = MyNumber(100)
print("repr(n1)返回的字符串是:", repr(n1))
print("str(n1)返回的字符串是:", str(n1))
