#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_属性受保护.py"""

import uuid

class Book(object):
    def __init__(self):
        self._isbn = uuid.uuid1()
    def show_isbn(self):
        return 'isbn : {}'.format(self._isbn)

b = Book()

print(b.__dict__)
print(b._isbn)
print(b.show_isbn())
