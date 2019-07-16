#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex09_change.py"""

# 改造前
def get_fullname(first_name, last_name):
    return f'{first_name} {last_name}'

print(get_fullname('xiao', 'ming'))

# 改造后
def get_fullname(*names):
    return ' '.join(names)

print(get_fullname('xiao', 'ming', 'leguan', 'tuatara'))
