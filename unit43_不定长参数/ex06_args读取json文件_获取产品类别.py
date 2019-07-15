#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex06_args读取json文件_获取产品类别.py"""


import json  # 需要该脚本文件的同级目录中有 northwind.json 文件


def show_categories(*cnames):
    print('所有类别名称如下：', end=' ')
    for name in cnames:
        print(name, end=', ')


# 获取数据时
with open('northwind.json', 'r') as f:
    data = json.loads(f.read())

categories = tuple({p['CategoryName'] for p in data})

show_categories(*categories)
