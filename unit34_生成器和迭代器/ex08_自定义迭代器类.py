#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_自定义迭代器类.py"""

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return Fib
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration
        return self.a

g = Fib()
print(next(g))
print(next(g))
print(next(g))
