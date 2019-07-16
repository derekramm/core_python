#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""helper.py"""

import json

from unit56_json模块案例.books import BookEncoder


def read_from_json(file='books.json'):
    '''
    读取JSON文件并返回字典格式的数据
    :param file: json文件的路径
    :return:
    '''
    with open(file, 'r') as f:
        return json.loads(f.read(), encoding='utf-8')


def write_to_json(books, file='books.json'):
    '''
    写入JSON文件
    :param books:
    :param file:
    :return:
    '''
    with open(file, 'w') as f:
        f.write(json.dumps(books, cls=BookEncoder))
