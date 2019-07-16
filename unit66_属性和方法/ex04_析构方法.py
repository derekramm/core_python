#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_析构方法.py"""

class Car(object):
    def __init__(self, name):
        self.name = name
        print('汽车',self.name,'对象已创建')
    def __del__(self):
        print('汽车',self.name,'对象已销毁')

c1 = Car('BYD E6')
c2 = Car('BYD E6')

# 注意执行顺序