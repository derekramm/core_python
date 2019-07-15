#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_斐波那契额数列.py"""

def fib():
    i, a, b = 0, 0, 1
    while i < 30:
        yield b
        a, b = b, a+b
        i += 1

g = fib()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
