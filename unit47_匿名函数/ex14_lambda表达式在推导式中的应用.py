#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex14_lambda表达式在推导式中的应用.py"""


func = [lambda x=i: i * i for i in range(4)]

print(func[0]())  # 9
print(func[1]())  # 9
print(func[2]())  # 9
print(func[3]())  # 9
