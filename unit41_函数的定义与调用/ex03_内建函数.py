#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_内建函数.py"""

# 输入输出函数
print(input('enter a number:'))

# 类型函数
type(True)
isinstance(True, bool)
print(zip(['a', 'b', 'c'], [1, 2, 3]))

# 数学函数
abs(-12)
divmod(12, 7)
pow(2, 3)
round(3.14)

# 全部条件判断函数
all([1, 0, 1, 0])
# 任一条件判断函数
any([1, 0, 1, 0])

# 进制转换函数
bin(10)
oct(10)
hex(10)

# 类型转换函数
int('1010', base=2)
float('3.14')
complex(1.0, 2.0)
bool(12)

# 序列转换函数
list(range(10))
tuple(range(10))
dict([('a', 'apple'), ('b', 'banana'), ('c', 'color')])
enumerate(['a', 'b', 'c'])

# 字符函数
chr(9801)
ord('♉')
eval('print("hello, world")')
'{}-{}'.format('xiao', 'ming')
str(12) + str(3)

# 序列函数
len('my name is xiaoming')
max(1, 3, 5, 7, 9, 2, 4, 6, 8, 0)
min(1, 3, 5, 7, 9, 2, 4, 6, 8, 0)

# 范围函数
range(10)

# 迭代器函数
iter(range(10))

