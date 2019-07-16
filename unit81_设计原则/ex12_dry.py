#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex12_dry.py"""

# 改造前
import sys
str_numa = input('请输入第一个数字：')
if str_numa.isdigit():
    numa = int(str_numa)
else:
    print('输入的数字不正确')
    sys.exit()

str_numb = input('请输入第二个数字：')
if str_numb.isdigit():
    numb = int(str_numb)
else:
    print('输入的数字不正确')
    sys.exit()

print(f'{numa} + {numb} = {numa + numb}')
