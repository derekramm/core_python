#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_分支结构代码示例.py"""

name = input('请输入你的姓名：')
gender = input('请输入你的性别：')

if gender == '男':
    print('欢迎你，{} 小哥哥'.format(name))

if gender == '女':
    print('欢迎你，{} 小姐姐'.format(name))
