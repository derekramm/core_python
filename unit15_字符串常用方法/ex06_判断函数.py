#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_判断函数.py"""

# isalnum()：是否只有字母数字构成
# isalpha()：是否只有字母构成
# isdecimal()：是否十进制数字
# isdigit()：判断是否是数字，包含次方位数字
# islower()：判断是否全部小写
# isupper()：判断是否全部大写
# isnumeric()：判断是否是数字，支持汉字
# isspace()：判断是否有空格
# istitle()：判断是否每个单词首字母大写
# isidentifier()：判断是否是有效的标识符

print('abc123'.isalnum())
print('abcABC'.isalnum())
print('1234567890'.isdecimal())
print('2⁴'.isdigit())
print('abc'.islower())
print('ABC'.isupper())
print('一二三四'.isnumeric())
print('   '.isspace())
print('Hello World'.istitle())
print('iden_18'.isidentifier())
