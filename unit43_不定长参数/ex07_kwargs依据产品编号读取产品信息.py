#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex07_kwargs依据产品编号读取产品信息.py"""

import json

# 获取数据时
with open('northwind.json', 'r') as f:
    data = json.loads(f.read())


def show_info(**kwargs):
    for k, v in kwargs.items():
        print('{}: {}'.format(k, v))


# 测试
show_info(**dict(编号=1, 名称='棒棒糖', 价格=10.99))

# 真实
show_info(**data[int(input('请输入产品编号（1-79）：')) - 1])