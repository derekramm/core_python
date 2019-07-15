#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_授权.py"""

from aip import AipFace

# 拼接请求

# 设置APP_ID、AK、SK,用于验证百度云应用
APP_ID = "15074363"
API_KEY = "Og53roYLkqAZgIpAKkuvGX07"
SECRECT_KEY = "ZwzdwgrqeZ1VasdXOUY3gGcd44jbbihs"
client = AipFace(APP_ID, API_KEY, SECRECT_KEY)