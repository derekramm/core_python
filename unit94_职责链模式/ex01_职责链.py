#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_职责链.py"""

from abc import ABCMeta, abstractmethod

class Chain(object, metaclass=ABCMeta):
    def __init__(self, level):
        self.next = None
        self.level = level
    def handle_request(self, level):
        if self.level >= level:
            self.show(level)
        elif self.next:
            self.next.handle_request(level)
        else:
            raise NotImplementedError
    @abstractmethod
    def show(self, level):
        pass

class ChainA(Chain):
    def show(self, level): print(f'ChainA show {level}')

class ChainB(Chain):
    def show(self, level): print(f'ChainB show {level}')

class ChainC(Chain):
    def show(self, level): print(f'ChainC show {level}')

if __name__ == '__main__':
    ca, cb, cc = ChainA(10), ChainB(100), ChainC(1000)
    ca.next = cb
    cb.next = cc
    ca.handle_request(10)
    ca.handle_request(100)
    ca.handle_request(1000)
