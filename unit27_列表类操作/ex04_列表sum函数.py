#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_列表sum函数.py"""

# sum 函数: 可以得到列表中所有元素的和: sum(列表[，起始值]), 起始值可以省略，缺省是0

a = [1, 2, 3]
print(sum(a))
print(sum(a, 10))

b = ["a", "b"]
sum(b)  # 报错
