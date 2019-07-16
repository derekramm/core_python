#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_str函数调用.py"""

class MyList:
    def __init__(self, iterable=[]):
        self.data = [x for x in iterable]
    def __str__(self):
        return "MyList(%s)" % self.data
    def __len__(self):
        return len(self.data)
    def __abs__(self):
        return MyList((abs(x) for x in self.data))

L = MyList([1, -2, 3, -4])
print(len(L))
print(abs(L))
