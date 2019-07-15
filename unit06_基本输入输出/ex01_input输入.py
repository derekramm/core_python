#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex01_input输入.py
输入函数 print： 用于接收用户从终端传入的参数
注意input函数返回类型都是字符串类型"""

name = input('请输入姓名：')
print(type(name), name)  # <class 'str'>

age = input('请输入年龄：')
print(type(age), age)  # <class 'str'>

score = input('请输入成绩：')
print(type(score), score)  # <class 'str'>
