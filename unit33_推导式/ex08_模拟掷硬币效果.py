#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_模拟掷硬币效果.py"""

from random import random
results = [int(round(random())) for x in range(10)]
print(results)
