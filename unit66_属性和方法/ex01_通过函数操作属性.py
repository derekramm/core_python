#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_通过函数操作属性.py"""

class Book(object):
    pass

b = Book()
print(b.__dict__)
if not hasattr(b, 'title'):
    setattr(b, 'title', 'python')
print(b.__dict__)
print(getattr(b, 'title'))
delattr(b, 'title')
# print(getattr(b, 'title'))