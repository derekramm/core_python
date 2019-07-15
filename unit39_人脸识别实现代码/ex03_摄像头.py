#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_连接.py"""
import base64

from aip import AipFace

# 拼接请求

# 设置APP_ID、AK、SK,用于验证百度云应用
APP_ID = "15074363"
API_KEY = "Og53roYLkqAZgIpAKkuvGX07"
SECRECT_KEY = "ZwzdwgrqeZ1VasdXOUY3gGcd44jbbihs"
client = AipFace(APP_ID, API_KEY, SECRECT_KEY)

with open(r"images/derek.jpg", "rb") as f:
    image = base64.b64encode(f.read())
    image = str(image, "utf-8")
    imageType = "BASE64"
    print(client.detect(image, imageType))

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    cv2.imshow('capture', frame)

