#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""shop.py"""
from unit56_json模块案例 import helper

books = helper.read_from_json('books.json')

for b in books:
    print(b)


def get_book_by_isbn(isbn):
    for b in books:
        if b['isbn'] == isbn:
            return b


if __name__ == '__main__':
    inp = input('please enter isbn: ')
    book = get_book_by_isbn(inp)
    print(book)
