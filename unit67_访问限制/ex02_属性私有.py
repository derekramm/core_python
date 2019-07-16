#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_属性私有.py"""

class Student(object):
    def __init__(self, name):
        self.name = name
        self.__age = 18

s = Student('xiaoming')
print(s.__dict__)

# print(s.__age)  # 会报错
print(s._Student__age)
