#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_访问私有属性.py"""

class Student(object):
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 0 <= age <= 100:
            self.__age = age

s = Student('xiaomign')
s.set_age(18)
print(s.get_age())