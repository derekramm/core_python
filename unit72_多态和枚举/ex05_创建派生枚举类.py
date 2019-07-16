#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_创建派生枚举类.py"""

from enum import Enum, unique

@unique
class Weekday(Enum):
    周日 = 0
    周一 = 1
    周二 = 2
    周三 = 3
    周四 = 4
    周五 = 5
    周六 = 6

for name, member in Weekday.__members__.items():
    print(name, member, member.value)
