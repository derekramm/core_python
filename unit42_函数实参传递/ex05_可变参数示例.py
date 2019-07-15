#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_可变参数示例.py"""

def add(names, name):
    names.append(name)
    print(names)

names = ['xiao', 'ming']
add(names, 'ramm')
add(names, 'derek')

print(names)  # 方法参数如果是可变类型，有可能在方法内部直接影响外部的变量
