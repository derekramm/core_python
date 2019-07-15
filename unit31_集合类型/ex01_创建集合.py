#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_创建集合.py"""

s = set()
print(s)
print(type(s))

s = set((1, 4, 2))
print(s)

s = set(["a", "c", "b"])
print(s)

s = set("123456")
print(s)

s = set({1: "yy", 2: "zz"})
print(s)

d = {1: "yy", 2: "zz"}
print(d)

s = set(d)
print(s)
