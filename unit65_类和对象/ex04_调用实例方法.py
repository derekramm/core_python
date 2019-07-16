#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_调用实例方法.py"""

class Dog(object):
    pass
    def eat(self, food):
        print('小狗正在吃', food)
    def sleep(self, hour):
        print('小狗睡了', hour, '小时')

d = Dog()
d.eat('骨头')
d.sleep(1)
Dog.eat(d, '狗粮')
Dog.sleep(d, 2)
