#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_自定义生成器.py"""

# 如果一个函数定义中包含 yield 关键字，那么这个函数就是一个生成器

def my_generator():
    print('step 01')
    yield (1)
    print('step 02')
    yield (2)
    print('step 03')
    yield (3)

g = my_generator()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
