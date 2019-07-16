#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_删除实例变量.py"""

class Student(object):
    pass

stu = Student()
stu.name = 'xiaoming'
stu.age = 18

print(stu.name, stu.age)
del stu.age
print(stu.name, stu.age)  # AttributeError: 'Student' object has no attribute 'age'
