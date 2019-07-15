#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_替换.py"""

# expandtabs()：替换制表符
# join()：拼接序列
# strip()：截取两端指定字符
# lstrip()：截取左侧指定字符
# rstrip()：截取右侧指定字符
# replace()：替换指定字符
# partition()：正向查找替换
# rpartition()：逆向查找替换
# translate()：按翻译表翻译
# maketrans()：设置翻译表

print('hello\tpython'.expandtabs(8))  # hello   python
print('hello\tpython'.expandtabs(16))  # hello           python
print(','.join('abcde'))  # a,b,c,d,e
print('**hello python**'.strip('*'))  # hello python
print('**hello python**'.lstrip('*'))  # hello python**
print('**hello python**'.rstrip('*'))  # **hello python
print('hello python'.replace('python','world'))  # hello world
print('hello python world'.partition(' '))  # ('hello', ' ', 'python world')
print('hello python world'.rpartition(' '))  # ('hello python', ' ', 'world')
print('apple banana color'.translate(str.maketrans('abc','123')))  # 1pple 21n1n1 3olor