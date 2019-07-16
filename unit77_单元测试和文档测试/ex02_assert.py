#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_assert.py"""

inp = input("请输入你的年龄: ")

assert inp.isdigit()
age = int(inp)  # 安全隐患:abc
print('成年' if age >= 18 else '未成年')
