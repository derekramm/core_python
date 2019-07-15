#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_分支嵌套.py"""

raw_username, raw_password = 'admin', '123456'

username = input('请输入用户名：')

if username == raw_username:
    password = input('请输入密码：')
    if password == raw_password:
        print('登录成功')
    else:
        print('密码不正确')
else:
    print('用户名不正确')
