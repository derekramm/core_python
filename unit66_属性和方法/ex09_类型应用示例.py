#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex09_类型应用示例.py"""

class Calculator(object):
    def __init__(self):
        self.numa = self.numb = None
    def add(self): return self.numa + self.numb
    def sub(self): return self.numa - self.numb
    def mul(self): return self.numa * self.numb
    def div(self): return self.numa / self.numb

c = Calculator()
c.numa, c.numb = 12, 3
print(
    c.add(),
    c.sub(),
    c.mul(),
    c.div()
)
