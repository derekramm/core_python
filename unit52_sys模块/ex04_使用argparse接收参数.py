#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex04_使用argparse接收参数.py"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', default='xiaoming')
parser.add_argument('-a', '--age', default=18)

# args = parser.parse_args('-n xiaoming -a 18'.split())
args = parser.parse_args()

print(args)
