#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_str函数重写.py"""

class MyClass:
    def __repr__(self):
        return 'MyClass()'

c = MyClass()
print(repr(c))  # MyClass()
print(str(c))  # MyClass()

class MyClass:
    def __repr__(self):
        return 'MyClass()'
    def __str__(self):
        return "我是字符串"

c = MyClass()
print(repr(c))  # MyClass()
print(str(c))  # 我是字符串
