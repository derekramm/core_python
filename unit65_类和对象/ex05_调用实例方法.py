#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_调用实例方法.py"""

class Teacher(object):
    def teaching(self, skill):
        return 'teaching {}'.format(skill)

class Student(object):
    def learning(self, skill):
        return 'learning {}'.format(skill)

t, s = Teacher(), Student()
print(t.teaching('python'))
print(s.learning('python'))
