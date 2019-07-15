#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_死循环.py"""

while True:
    str_num = input('请输入十进制整数：')
    if str_num.isdigit():
        print('转换成二进制是：', bin(int(str_num)))
    else:
        if input('格式不正确，要重新输入吗？（y/n）：') == 'y':
            continue
        else:
            break
