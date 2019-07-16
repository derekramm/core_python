#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_循环绘制正方形.py"""

import turtle

turtle.color('red', 'yellow')
turtle.speed(10)

for i in range(50):
    turtle.forward(i * 5)
    turtle.right(90)

turtle.done()
