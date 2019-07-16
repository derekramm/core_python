#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex02_接收命令行参数.py"""

# !/usr/bin/env python3
# -*- conding=utf-8 -*-

import sys

VERSION = '1.0'


def help(argv0):
    print('使用方法：')
    print("cmdline [-h -v]")
    print('''-h  显示帮助信息\
             \n-v  显示版本信息''')
    return


def version():
    print('cmdline version is :', VERSION)
    return


def main():
    i = 0
    for argv in sys.argv:
        if argv == '-v':
            version()
        elif argv == '-h':
            help(sys.argv[0])


main()
