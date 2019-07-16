#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_简单工厂原型pythonic.py"""

class Product(object): pass

class ProductA(Product): pass

class ProductB(Product): pass

def get_product(product_name):
    if product_name == 'a':
        return ProductA()
    elif product_name == 'b':
        return ProductB()
    else:
        return None

if __name__ == '__main__':
    print(get_product('a'))
    print(get_product('b'))
    print(get_product('c'))
