#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_太阳花.py"""

import turtle
turtle.color("red", "yellow")
turtle.speed(10)
turtle.begin_fill()

for _ in range(36):
    turtle.forward(200)
    turtle.left(170)

turtle.end_fill()

turtle.mainloop()
