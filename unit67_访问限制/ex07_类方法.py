#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_类方法.py"""

class Student(object):
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def set_count(cls, value):
        cls.count = value

print(Student.get_count())
Student.set_count(10)
print(Student.get_count())
