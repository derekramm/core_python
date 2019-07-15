#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_连接.py"""

import base64
import time

import cv2
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

    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('s'):
        file_name = 'opencv_images/' + str(time.time()) + '.jpg'
        cv2.imwrite(file_name, frame)

        """ 如果有可选参数 """
        options = {
            "face_field": "age,beauty,expression,faceshape,gender,glasses,landmark,race,quality,facetype",
            "max_face_num": 3,
            "face_type": "LIVE"
        }

        with open(file_name, "rb") as f:
            image = base64.b64encode(f.read())
            image = str(image, "utf-8")
            imageType = "BASE64"
            data = client.detect(image, imageType, options)
