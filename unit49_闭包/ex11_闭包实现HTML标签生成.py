#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex11_闭包实现HTML标签生成.py"""


# 使用闭包实现HTML标签的生成

def tag(tag_name):
    def add_tag(content):
        return "<{0}>{1}</{0}>".format(tag_name, content)

    return add_tag


content = 'Hello'

add_tag = tag('a')
print(add_tag(content))
# <a>Hello</a>

add_tag = tag('b')
print(add_tag(content))
# <b>Hello</b>
