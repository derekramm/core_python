#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_集合推导式.py"""

names = [1, 3, "Name", "Mob"]
s = {n for n in names}
print(s)
names = [1, 3, "Name", "Mob"]
s = {n for n in names if n != 3}
print(s)

