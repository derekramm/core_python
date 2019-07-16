#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_lsp.py"""

class Person(object):
    def __init__(self, name):
        self.name = name
    def talk(self): return f'my name is {self.name}'

class Teacher(Person):
    def talk(self): return f'i am a teacher and {super().talk()}'

class Cat(object):
    @staticmethod
    def talk(): return '喵喵喵~~~'

def show(person): print(person.talk())

show(Person('dxy'))
show(Teacher('xm'))
show(Cat)
