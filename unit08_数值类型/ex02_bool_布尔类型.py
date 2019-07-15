#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_bool_布尔类型.py"""

"""
布尔型是整型的子类，用来表示真和假两种对立的状态
True 表示真（条件满足或成立），False 表示假（条件不满足或不成立）
True  值为1，False 值为0
"""

# 通过type()判断 True 和 False 的类型
print(type(True))  # <class 'bool'>  布尔类型
print(type(False))  # <class 'bool'>

# 虽然是布尔类型，但是通过 isinstance(True, int) 判断 True 是否为 int 整型
# 如果是整型返回 True，反之 False
print(isinstance(True, int))  # True
print(isinstance(True, float))  # False

# 通过 == 判断True的值是否为1
print(True == 1)
print(True + 2)  # 对True做加法（算数）运算：3

# 通过 == 判断False的值是否为0
print(False == 0)
print(False - 5)  # # 对False做加法（算数）运算：-5

print(True + False)  # 1
