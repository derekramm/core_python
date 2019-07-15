#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_随机加法计算器.py"""

import random

score = 0

for _ in range(5):
    a, b = random.randint(1, 10), random.randint(1, 10)
    result = a + b
    answer = int(input('{}+{}=?'.format(a, b)))
    if result == answer:
        score += 1

print('一共答对了{}道题'.format(score))
