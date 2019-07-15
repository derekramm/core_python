#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_is和==的区别.py"""

age1 = -8
age2 = -8
print("age1的id地址为：{}".format(id(age1)))  #  age1的id地址为：140097719334032
print("age2的id地址为：{}".format(id(age2)))  #  age2的id地址为：140097719334064
print('age1==age2的结果：', age1 == age2)  #  age1==age2的结果： True
print('age1 is age2的结果：', age1 is age2)  #  age1 is age2的结果： False
