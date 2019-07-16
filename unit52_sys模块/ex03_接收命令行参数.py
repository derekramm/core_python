#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex03_接收命令行参数.py"""

import sys


def add(a, b):
    return a + b


if __name__ == '__main__':
    numa, numb = int(sys.argv[1]), int(sys.argv[2])
    print('{}+{}={}'.format(numa, numb, numa + numb))
