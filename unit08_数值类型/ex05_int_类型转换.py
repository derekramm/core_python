#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_int_类型转换.py"""

"""
作用：int函数用于将一个字符串或者数字转化为整型，
如果没有参数则返回 0
语法：int(obj, base=10)
参数说明：obj 为数字或者字符串，base 指进制，有效的基数是 0 和 2-36
"""

print(32.5)
print(int(32.5))  # 小数转整数

print('32')
print(int('32'))  # 字符串转整数

print('1011')
print(int('1011', base=2))  # 11

print('77')
print(int('77', base=8))  # 63

print('FF')
print(int('FF', base=16))  # 255