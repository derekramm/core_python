#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex02_eval_input.py
可以通过eval函数解释接收到的字符串"""

name = input('请输入姓名：')  # 这里在终端输入 ''
print(type(eval(name)))

age = input('请输入年龄：')  # 这里在终端输入 18
print(type(eval(age)))  # <class 'int'>

score = input('请输入成绩：')  # 这里在终端输入 85.5
print(type(eval(score)))  # <class 'float'>
