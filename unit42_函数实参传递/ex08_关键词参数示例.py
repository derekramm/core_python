#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_关键词参数示例.py"""

def get_area(top, bottom, height):
    print((top + bottom) * height / 2)  # 梯形面积 = (上底 + 下底) * 高 / 2

get_area(10, height=20, bottom=90)  # 关键字参数和必备参数混用时，需要放置在最后
