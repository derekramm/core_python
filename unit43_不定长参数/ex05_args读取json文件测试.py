#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex05_args读取json文件测试.py"""

import json  # 需要该脚本文件的同级目录中有 northwind.json 文件


def show_categories(*cnames):
    print('所有类别名称如下：', end=' ')
    for name in cnames:
        print(name, end=', ')


# 测试
print('测试')
show_categories('饮料类', '调味品', '水果')
