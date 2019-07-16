#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_class属性.py"""

class Dog(object):
    pass

d1 = Dog()
print(d1.__class__)
d2 = d1.__class__()
print(d2)
print(d2.__class__)
