#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_格式化位置.py"""

# center()：指定长度并居中
# ljust()：左对齐
# rjust()：右对齐
# zfill()：指定长度并补零

print('hello'.center(20, '-'))  # -------hello--------
print('dxy'.ljust(20, '-'))  # dxy-----------------
print('xm'.rjust(20, '-'))  # ------------------xm
print('18'.zfill(20))  # 00000000000000000018