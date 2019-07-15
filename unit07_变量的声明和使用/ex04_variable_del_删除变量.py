#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex04_variable_del_删除变量.py
删除变量"""

name, age, gender = '小铭', 18, False
print(f'name:{name}, age:{age}, gender:{gender}')  # name:小铭, age:18, gender:False

del age, gender  # 同时删除多个变量

try:
    # 删除变量后不能再次使用
    print(f'name:{name}, age:{age}, gender:{gender}')
except Exception as ex:
    print(ex)  # name 'age' is not defined
