#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_类变量.py"""

class Person(object):
    total_count = 0
    def __init__(self, name):
        self.name = name
        self.__class__.total_count += 1

print(Person.total_count)
Person('xiaoming')
print(Person.total_count)
Person('leguan')
print(Person.total_count)
