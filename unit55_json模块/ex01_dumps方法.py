#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex01_dumps方法.py"""
import doctest


def test():
    """
    >>> import json
    >>> json.dumps([])    # dumps可以格式化所有的基本数据类型为字符串
    '[]'
    >>> json.dumps(1)    # 数字
    '1'
    >>> json.dumps('1')   # 字符串
    '"1"'
    >>> dict = {"name":"xiaoming", "age":18}
    >>> json.dumps(dict)     # 字典
    '{"name": "xiaoming", "age": 18}'
    """

if __name__ == '__main__':
    doctest.testmod()