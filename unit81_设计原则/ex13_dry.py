#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex13_dry.py"""

# 改造后
import sys

def check_num(n):
    if n.isdigit():
        return int(n)
    else:
        print('输入的数字不正确')
        sys.exit()

numa = check_num(input('请输入第一个数字：'))
numb = check_num(input('请输入第二个数字：'))

print(f'{numa} + {numb} = {numa + numb}')
