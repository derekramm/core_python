#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_装饰器单例.py"""

def singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

@singleton
class A(object): pass

a1, a2 = A(), A()
print(a1 is a2, id(a1), id(a2))
