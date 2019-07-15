#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_统计查找.py"""

# count()：指定字符出现的次数
# find()：正向查找出现的位置
# rfind()：逆向查找出现的位置
# index()：正向查找出现的位置（异常）
# rindex()：逆向查找出现的位置（异常）
# endswith()：判断是否以指定字符结尾
# startswith()：判断是否以指定字符开始
# min()：查找最小字符
# max()：查找最大字符
# split()：拆分
# splitlines()：按行拆分

print('hello world'.count('l'))  # 3
print('hello world'.find('l'))  # 2
print('hello world'.rfind('l'))  # 9
print('hello world'.index('o'))  # 4
print('hello world'.rindex('o'))  # 7
print('hello world'.endswith('world'))  # True
print('hello world'.startswith('hello'))  # True
print(min('python'))  # h
print(max('python'))  # y
print('hello world'.split())  # ['hello', 'world']
print('''hello
guido
van
rossum'''.splitlines())  # ['hello', 'guido', 'van', 'rossum']


