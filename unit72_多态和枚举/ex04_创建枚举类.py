#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_创建枚举类.py"""

from enum import Enum
Season = Enum('Season', ('Spring', 'Summer', 'Fall', 'Winter'))
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Season.Spring, Season.Summer, Season(3), Season(4))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
