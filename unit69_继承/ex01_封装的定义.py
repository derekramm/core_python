#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_封装的定义.py"""

class Cat(object):
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def info(self):
        return 'i am a {} cat, my name is {}, i am {} years old'.format(self.color, self.name, self.age)

cat01 = Cat('tom', 2, 'black')
cat02 = Cat('kitty', 3, 'white')
print(cat01.info())
print(cat02.info())
