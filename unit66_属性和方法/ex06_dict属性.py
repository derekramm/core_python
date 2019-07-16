#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_dict属性.py"""

class Dog(object):
    pass

d = Dog()
print(d.__dict__)
d.kinds = '拉布拉多'
print(d.__dict__)
d.color = '白色'
print(d.__dict__)
