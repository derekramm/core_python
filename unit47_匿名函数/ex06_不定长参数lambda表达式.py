#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex06_不定长参数lambda表达式.py"""

func = lambda **kwargs: (kwargs.keys(), kwargs.values())

print(func(a='apple', b='banana'))

# (dict_keys(['a', 'b']), dict_values(['apple', 'banana']))
