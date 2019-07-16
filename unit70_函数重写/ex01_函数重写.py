#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_函数重写.py"""

# 重写后
class MyClass:
    def __len__(self):
        return 100

obj = MyClass()
print(len(obj))
