#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_依赖关系.py"""

class Pycharm(object):
    def editing(self):
        return self.__class__.__name__

class Python(object):
    def programming(self, pycharm):
        return f'using {pycharm.editing()} write {self.__class__.__name__}'

print(Python().programming(Pycharm()))
