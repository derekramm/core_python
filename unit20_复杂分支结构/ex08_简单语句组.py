#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_简单语句组.py"""

import datetime

today = datetime.date.today()
day_of_week = datetime.date.weekday(today)

if day_of_week >= 5: print('今天是周末')
if day_of_week < 5: print('今天是工作日', day_of_week)
