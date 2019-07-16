#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex13_lambda表达式在推导式中的应用.py"""

func = [lambda i=i: i * i for i in range(4)]

print(func[0]())  # 0
print(func[1]())  # 1
print(func[2]())  # 4
print(func[3]())  # 9
