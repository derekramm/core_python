#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_complex.py"""

# 复数由【实部 + 虚部】组成，默认都是浮点类型
# 语法：real+imagej

cp = 1.0 + 0.3j
print(cp)  # 打印cp复数
print(cp.real)  # cp.real打印复数实部
print(cp.imag)  # cp.imag打印复数虚部
print(cp.conjugate())  # cp.conjugate()打印共轭复数
