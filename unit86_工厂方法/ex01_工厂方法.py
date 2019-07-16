#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_工厂方法.py"""
from abc import ABCMeta, abstractmethod

class Product(object): pass  # 父类产品

class ProductA(Product): pass  # 子类产品A

class ProductB(Product): pass  # 子类产品B

class Factory(metaclass=ABCMeta):  # 父类工厂
    # 静态方法：根据用户参数实例化具体子类工厂
    @staticmethod
    def choose_factory(factory_name='a'):
        factories = dict(a=FactoryA, b=FactoryB)
        return factories[factory_name]()
    @abstractmethod
    def get_product(self): pass  # 抽象方法：获取产品

class FactoryA(Factory):  # 子类工厂A, 负责生产自类产品A
    def get_product(self): return ProductA()

class FactoryB(Factory):  # 子类工厂B, 负责生产自类产品B
    def get_product(self): return ProductB()

if __name__ == '__main__':
    print(Factory.choose_factory('a').get_product())
    print(Factory.choose_factory('b').get_product())
