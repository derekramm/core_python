#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex06_随机生成四位验证码.py"""

import random

# 生成一个包含大写字母A-Z和数字0-9的随机4位验证码
checkcode = ''
for i in range(4):
    current = random.randrange(0, 4)
    if current != i:
        temp = chr(random.randint(65, 90))
    else:
        temp = random.randint(0, 9)
    checkcode += str(temp)
print(checkcode)
