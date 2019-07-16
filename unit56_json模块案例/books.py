#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""books.py"""

import json


class Book(object):
    def __init__(self, isbn, title, author, price, pubdate):
        self.isbn = isbn
        self.title = title

        self.author = author
        self.price = price
        self.pubdate = pubdate

    def __str__(self):
        return str(self.__dict__)


class BookEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Book):
            return o.__dict__
        return json.JSONEncoder.default(self, o)
