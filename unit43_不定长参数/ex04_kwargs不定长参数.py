#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex04_kwargs不定长参数.py"""

def greet(**kwargs):
    for key, value in kwargs.items():
        print('{} = {}'.format(key, value))


greet(name='xiaoming', age=18, gender=False)
