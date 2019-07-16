#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_静态方法.py"""

class MyClass(object):
    @staticmethod
    def my_func(fname, lname):
        return fname + lname

print(MyClass.my_func('xiao', 'ming'))
