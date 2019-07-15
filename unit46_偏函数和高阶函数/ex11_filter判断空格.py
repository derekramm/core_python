#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex11_filter判断空格.py"""


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
