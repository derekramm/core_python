#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_lsp.py"""

class Person(object):
    def __init__(self, name):
        self.name = name
    def talk(self): return f'my name is {self.name}'

class Teacher(Person):
    def talk(self): return f'i am a teacher and {super().talk()}'

def show(person): print(person.talk())

show(Person('dxy'))
show(Teacher('xm'))
