#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_文档测试.py"""

import doctest

def test(x):
    """
    >>> test(2)
    'even'
    >>> test(1)
    'odd'
    """
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'

if __name__ == '__main__':
    doctest.testmod()