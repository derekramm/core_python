#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_循环等待输入.py"""

# 循环等待输入
while True:
    s = input("请输入字符串(exit 退出):")
    if s == "exit":
        break
    print("input is", s)
