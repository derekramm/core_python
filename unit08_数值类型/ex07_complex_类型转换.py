#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_complex_类型转换.py"""

'''
函数用于创建一个值为 real + imagj 的复数或者转化一个字符串或数为复数
如果第一个参数为字符串，则不需要指定第二个参数
语法：complex(real[, imag])，返回值：复数
参数说明：real 为实部，imag 为可选虚部，默认为 0
'''

print(complex('1+3j'))  # 将字符串转化为复数型,结果为1+3j
print(complex(2, 3))  # 将整型转为复数型, 结果为2+3j
print(complex(1.2, 2))  # 将浮点型转为复数型， 结果为1.2+2j
