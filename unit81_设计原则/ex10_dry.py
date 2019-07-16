#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex10_dry.py"""

# 改造前
names = ['xm', 'dxy']

def isexist(name, names):
    return (name in names)

def add_name(name, names):
    if name not in names:
        names.append(name)

print(isexist('xiaoming', names))
add_name('xiaoming', names)
print(isexist('xiaoming', names))
