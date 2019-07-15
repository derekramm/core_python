#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_pass语句示例.py"""

import random

lucky_num = random.randint(1, 10)
print('随机生成的数字是:', lucky_num)

if lucky_num == 6:
    print('获得幸运数字:', lucky_num)
else:
    pass
