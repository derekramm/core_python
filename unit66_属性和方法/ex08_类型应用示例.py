#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_类型应用示例.py"""

class Cat(object):
    def __init__(self, *args):
        self.name, self.age, self.color, self.gender = args
    def eating(self, food):
        print('{} is eating {}'.format(self.name, food))

c = Cat('汤姆', 1, '白色', True)
print(c.__class__)
print(c.__dict__)
c.eating('小鱼干')
