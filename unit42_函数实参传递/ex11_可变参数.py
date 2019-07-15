#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex11_可变参数.py"""

def get_total(*args):
    print(sum(args))

get_total(1, 2, 3, 4)
get_total(*(1, 2, 3, 4))