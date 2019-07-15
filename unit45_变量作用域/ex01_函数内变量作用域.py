#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex01_函数内变量作用域.py"""


# 变量创建后，作用域就确定了
# 函数内创建的变量，只能被函数内的代码访问，不能被函数外的代码访问

def func():
    name = 'xiaoming'


print(name)  # NameError: name 'name' is not defined
