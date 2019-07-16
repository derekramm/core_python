#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_定义类.py"""

class MyClass(object):
    pass

mc = MyClass()

print(MyClass)  # <class '__main__.MyClass'>
print(mc)  # <__main__.MyClass object at 0x102d940b8>

class Dog:
    pass

dog1 = Dog()
dog2 = Dog()

print(id(dog1), id(dog2))
