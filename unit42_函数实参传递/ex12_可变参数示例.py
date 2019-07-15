#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex12_可变参数示例.py"""


def show_info(**kwargs):
    for k in kwargs:
        print(k, kwargs[k])


show_info(**{'a': 'apple', 'b': 'banana', 'c': 'color'})
show_info(**dict(c='cat', d='dog', m='mouse'))
