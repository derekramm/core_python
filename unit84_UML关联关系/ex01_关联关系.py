#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_关联关系.py"""

class Publisher(object):
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name

class Book(object):
    def __init__(self, isbn, title, author, price, pubdate, publisher):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.pubdate = pubdate
        self.publisher = publisher
