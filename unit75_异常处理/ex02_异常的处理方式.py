#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_异常的处理方式.py"""

inp = input("请输入你的年龄: ")

try:
    age = int(inp)  # 安全隐患:abc
    print('成年' if age >= 18 else '未成年')
except:
    print("无效的年龄格式,请重新输入!")
