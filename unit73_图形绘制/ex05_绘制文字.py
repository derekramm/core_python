#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_绘制文字.py"""

import turtle
turtle.screensize(400, 400, 'pink')
turtle.color('red')
turtle.hideturtle()  # 隐藏画笔
turtle.penup()  # 提起画笔移动
turtle.goto(-260, 10)  # 移动画笔位置
turtle.write('达内直播课', font=('娃娃体-简', 100, 'bold'))
turtle.hideturtle()
turtle.done()
