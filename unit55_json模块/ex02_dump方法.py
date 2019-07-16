#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex02_dump方法.py"""

import json

a = {"name": "xiaoming", "age": 18}

with open("xm.json", "w", encoding='utf-8') as f:
    # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
    f.write(json.dumps(a, indent=4, sort_keys=True))
    # json.dump(a,f,indent=4)   # 和上面的效果一样
