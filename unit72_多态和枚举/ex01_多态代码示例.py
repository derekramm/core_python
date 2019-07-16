#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_多态代码示例.py"""

class Bird:
    def move(self, field):
        print(f'小鸟在{field}中自由的飞翔')

class Dog:
    def move(self, field):
        print(f'小狗在{field}上快乐的奔跑')

x = Bird()
x.move('天空')
x = Dog()
x.move('草地')
