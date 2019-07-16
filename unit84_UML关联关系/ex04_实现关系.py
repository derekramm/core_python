#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_实现关系.py"""

from abc import ABCMeta, abstractmethod

class Drawable:
    __metaclass__ = ABCMeta
    @abstractmethod
    def draw(self): pass

class Cicle(Drawable):
    def draw(self): return '绘制圆形'

c = Cicle()
print(c.draw())
