#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_代码复用.py"""

class Cal(object):
    def __init__(self, numa, numb):
        self.numa = numa
        self.numb = numb
    def get_result(self): pass

class Add(Cal):
    def __init__(self, na, nb):
        super(Add, self).__init__(na, nb)
    def get_result(self): return self.numa + self.numb

class Sub(Cal):
    def __init__(self, na, nb):
        super(Sub, self).__init__(na, nb)
    def get_result(self): return self.numa - self.numb
