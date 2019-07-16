#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_布尔测试函数重写示例.py"""

class A: pass

a = A()
print(bool(a))

class A:
    def __len__(self): return 0

a = A()
print(bool(a))

class A:
    def __len__(self): return 1
    def __bool__(self): return False

a = A()
print(bool(a))
