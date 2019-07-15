#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex11_global_nonlocal.py"""

# global 声明变量为顶层全局变量，可用于任何函数
# nonlocal声明变量为嵌套函数中的上一层变量（非本地）

x = 100
def func():
    x = 1000
    def func2():
        global x
        x = 2000
    func2()
    print(x)

print(x)  # 100
func()    # 1000
print(x)  # 2000


x = 100
def func():
    x = 1000
    def func2():
        nonlocal x
        x = 2000
    func2()
    print(x)

print(x)  # 100
func()    # 2000
print(x)  # 100