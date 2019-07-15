#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""dal.py"""

import random
import unit35_实体模型和列表的应用.db

# 随机挑出两种水果
def get_fruit():
    return random.sample(unit35_实体模型和列表的应用.db.fruits, 2)
