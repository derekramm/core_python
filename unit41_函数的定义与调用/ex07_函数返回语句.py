#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_函数返回语句.py"""

import datetime

def get_day_of_week():
    dow = datetime.date.weekday(datetime.date.today())
    if dow in range(5):
        return '工作日'
    else:
        return '休息日'

print(get_day_of_week())
