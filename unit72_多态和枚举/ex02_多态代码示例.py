#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_多态代码示例.py"""

class Canvas:
    def draw(self, shape):
        print('开始绘制'.center(27, '-'))
        shape.draw(self)

class Rectangle:
    def draw(self, canvas):
        print(f'在{canvas}上绘制矩形')

class Triangle:
    def draw(self, canvas):
        print(f'在{canvas}上绘制三角形')

class Circle:
    def draw(self, canvas):
        print(f'在{canvas}上绘制圆形')

c = Canvas()
c.draw(Rectangle())
c.draw(Triangle())
c.draw(Circle())
