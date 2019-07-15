#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex12_sorted高阶函数_排序.py"""

# sorted() 函数就可以对list进行排序，默认降序；
# 它还可以接收一个key函数来实现自定义的排序


books = [
    dict(title='python', author='guido', price=20),
    dict(title='java', author='james', price=10),
    dict(title='c#', author='andrus', price=30)
]


def byprice(b):
    return b['price']


print(books)
print(sorted(books, key=byprice))
