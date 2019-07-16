#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex03_load方法.py"""

import json

with open("xm.json", "r", encoding='utf-8') as f:
    data1 = json.loads(f.read())

    f.seek(0)
    data2 = json.load(f)

print(data1)
print(data2)
