#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_五角星.py"""

import turtle

turtle.pensize(5)
turtle.speed(10)
turtle.pencolor("yellow")
turtle.fillcolor("red")

turtle.begin_fill()

for _ in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()

turtle.mainloop()
