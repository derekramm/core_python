#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_初始化方法示例.py"""

class Car(object):
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model
    def run(self, speed):
        print(self.color, '的', self.brand, self.model, '以', speed, '公里的速度行驶')

a4 = Car('红色', '奥迪', 'A4')
a4.run(199)
