#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_属性装饰器.py"""

class Dog(object):
    def __init__(self):
        self.__name = None
        self.__age = None
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

d = Dog()
d.name = 'Tom'
print(d.name)
