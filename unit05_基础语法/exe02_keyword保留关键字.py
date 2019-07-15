#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""exe02_keyword保留关键字.py"""

# 1、通过 keyword.kwlist 可以打印出 python 中所有保留关键字
# 2、通过 keyword.iskeyword() 可以判断是否为关键字，如果是关键字，返回 True，反之为 False

import keyword  # 导入模块

# 运行打印出所有的保留关键字
print(keyword.kwlist)
'''输出结果
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']'''

# 判断'str'是否为关键字
print(keyword.iskeyword("str"))  # False
