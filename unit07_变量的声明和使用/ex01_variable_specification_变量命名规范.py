#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex01_variable_specification_变量命名规范.py
判断下面的变量名是否命名规范"""

print('a {%s}' % 'a'.isidentifier())
print('_name {%s}' % '_name'.isidentifier())
print('myAge {%s}' % 'myAge'.isidentifier())
print('my_Name {%s}' % 'my_Name'.isidentifier())
print('num1 {%s}' % 'num1'.isidentifier())
print('num_ {%s}' % 'num_'.isidentifier())
print('$abc {%s}' % '$abc'.isidentifier())  # $abc {False}
print('1_Num {%s}' % '1_Num'.isidentifier())  # 1_Num {False}
print('class {%s}' % 'class'.isidentifier())  # 注意：命名规范但是是关键字
print('print {%s}' % 'print'.isidentifier())  # 注意：命名规范但是是关键字
