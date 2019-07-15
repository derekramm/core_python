#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""exe01_定义变量.py
python中定义变量只能有字母、数字、下划线构成
字母：区分大小写，
数字：不能做为标识符开头
下划线：由特定含义"""

# name和Name是两个完全不同的变量
name = '小铭'
Name = '大蜥蜴'
print(name, Name)  # 小铭 大蜥蜴

# 切记不能以数字开头，例如：【1num】（错误变量名）
num1 = 12
print(num1)  # 12

# 下划线如果需要和系统区分，需在变量名后面加
print_ = '输出函数'
print(print_)  # 输出函数
