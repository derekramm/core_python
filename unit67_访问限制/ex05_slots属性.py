#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_slots属性.py"""

class Student(object):
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student('xiaoming', 18)
s.gender = False