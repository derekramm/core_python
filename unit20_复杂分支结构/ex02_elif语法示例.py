#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_elif语法示例.py"""

score = int(input('请输入考试成绩:'))

if score >= 85:
    print('优秀')
elif 60 <= score < 85:
    print('合格')
else:
    print('不及格')
