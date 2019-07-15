#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex11_input_redirect_输入重定向.py
输入重定向"""

import sys

with open('the_zen_of_python.txt', 'r+') as zop:
    sys.stdin = zop  # 将输入重定向到指定的文件
    print(sys.stdin.read())  # 读取文件中的内容并输出到终端
