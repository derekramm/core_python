#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_析构方法.py"""

class Car(object):
    def __init__(self, name):
        self.name = name
        print('汽车', self.name, '对象已创建')
    def __del__(self):
        print('汽车', self.name, '对象已销毁')

print(id(Car('BYD E6')), id(Car('BYD E6')))
# 注意执行顺序
