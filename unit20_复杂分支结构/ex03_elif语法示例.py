#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_elif语法示例.py"""

day = int(input('请输入请假的天数:'))

if day <= 1:
    print('找经理请假')
elif 1 < day <= 2:
    print('找总监请假')
elif 2 < day <= 3:
    print('找老板请假')
else:
    print('直接回家了')
