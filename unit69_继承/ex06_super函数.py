#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_super函数.py"""

class A:
    def __init__(self, name):
        self.name = name
        print("父类的__init__方法被执行了！")
    def show(self):
        print("父类的show方法被执行了！")

class B(A):
    def __init__(self, name, age):
        super(B, self).__init__(name=name)
        self.age = age
    def show(self):
        super(B, self).show()

obj = B("jack", 18)
obj.show()
