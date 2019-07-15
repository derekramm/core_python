#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_必备参数.py"""

def sub(num1, num2):
    print('{} - {} = {}'.format(num1, num2, num1 - num2))

sub(12, 3)
sub(3, 12)
sub(*(12, 3))
sub(*(3, 12))
