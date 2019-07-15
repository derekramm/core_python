#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_不可变参数.py"""

def swap(num1, num2):
    num1, num2 = num2, num1
    print('num1={}, num2={}'.format(num1, num2))


m, n = 12, 3

swap(m, n)
print('num1={}, num2={}'.format(m, n))  # 方法执行后并不会影响原有的数据
