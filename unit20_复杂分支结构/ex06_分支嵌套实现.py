#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_分支嵌套实现.py"""

ticket_price = 100

month = int(input('请输入月份:'))
age = int(input('请输入年龄:'))

if month not in (4, 5, 6, 7, 8):
    ticket_price *= 0.8
    if any([age <= 12, age >= 70]):
        ticket_price *= 0.6

print('应收金额:', ticket_price)
