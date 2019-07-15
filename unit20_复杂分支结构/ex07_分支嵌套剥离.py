#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_分支嵌套剥离.py"""


def check_password():
    password = input('请输入密码：')
    if password == '123456':
        print('登录成功')
    else:
        print('密码不正确')


username = input('请输入用户名：')
if username == 'admin':
    check_password()
else:
    print('用户名不正确')
