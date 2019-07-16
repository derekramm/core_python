#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_防御式编码.py"""

inp = input("请输入你的年龄: ")

if inp.isdigit():
    age = int(inp)  # 安全隐患:abc
    print('成年' if age >= 18 else '未成年')
else:
    print("无效的年龄格式,请重新输入!")