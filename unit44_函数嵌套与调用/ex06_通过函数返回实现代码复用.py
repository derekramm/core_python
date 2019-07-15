#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex06_通过函数返回实现代码复用.py"""

# 初始化图书集合

books = [
    dict(title='红楼梦', author='曹雪芹', price=10),
    dict(title='西游记', author='吴承恩', price=20),
    dict(title='水浒传', author='施耐庵', price=30),
    dict(title='三国演义', author='罗贯中', price=40)
]


# 编写根据标题查找图书的方法，条件符合时返回图书字典，没有查询到时返回 None

def get_by_title(title):
    for b in books:
        if b['title'] == title:
            return b


print(get_by_title('三国演义'))
print(get_by_title('三国志'))  # None
