#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_元组的访问.py"""

t = (1, "yy", (2, 3, 4), 22)
print(t)

print(t[1])
print(t[0])
print(t[2])
print(t[2][0])
print(t[-1])
print(t[:])

try:
    print(t[4])
except Exception as ex:
    print(ex)  # tuple index out of range
