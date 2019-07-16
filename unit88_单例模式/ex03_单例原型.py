#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_单例原型.py"""

class Singleton(object):

    @classmethod
    def instance(cls):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = cls()
        return Singleton._instance

if __name__ == '__main__':
    s1, s2 = Singleton(), Singleton()
    print(id(s1), id(s2))

