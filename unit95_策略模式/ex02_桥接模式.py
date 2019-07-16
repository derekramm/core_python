#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_桥接模式.py"""

from abc import ABCMeta, abstractmethod

class IFunc(metaclass=ABCMeta):
    @abstractmethod
    def handle(self): pass

class FuncA(IFunc):
    def handle(self): return self.handle

class FuncB(IFunc):
    def handle(self): return self.handle

class Product:
    def __init__(self):
        self.kvs = dict()
    def add(self, k, v): self.kvs[k] = v
    def remove(self, k): del self.kvs[k]
    def get(self, k): return self.kvs[k]
    @abstractmethod
    def request(self, k): pass

class ProductA(Product):
    def request(self, k): return self, self.kvs[k].handle()

class ProductB(Product):
    def request(self, k): return self, self.kvs[k].handle()

if __name__ == '__main__':
    pa = ProductA()
    pb = ProductB()

    pa.add('a', FuncA())
    pa.add('b', FuncB())
    pb.add('a', FuncA())
    pb.add('b', FuncB())

    print(pa.request('a'))
    print(pa.request('b'))
    print(pb.request('a'))
    print(pb.request('b'))
