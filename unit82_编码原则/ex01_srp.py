#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_srp.py"""

# 改造前

def calculator(numa, numb, op):
    if op == '+':
        return numa + numb
    elif op == '-':
        return numa - numb
    elif op == '*':
        return numa * numb
    elif op == '/':
        return numa / numb
    else:
        return None

print(calculator(12, 3, '+'))
print(calculator(12, 3, '-'))
print(calculator(12, 3, '*'))
print(calculator(12, 3, '/'))
print(calculator(12, 3, '%'))
