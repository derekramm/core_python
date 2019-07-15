#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_代码显示.py"""

import base64

from aip import AipFace

""" 你的 APPID AK SK """
__APP_ID = '15074363'
__API_KEY = 'Og53roYLkqAZgIpAKkuvGX07'
__SECRET_KEY = 'ZwzdwgrqeZ1VasdXOUY3gGcd44jbbihs'

__client = AipFace(__APP_ID, __API_KEY, __SECRET_KEY)


def detect(img_url):
    with open(img_url, 'rb') as f:
        image = str(base64.b64encode(f.read()), 'utf-8')
    image_type = "BASE64"

    """ 如果有可选参数 """
    options = {
        "face_field": "age,beauty,expression,faceshape,gender,glasses,landmark,race,quality,facetype",
        "max_face_num": 3,
        "face_type": "LIVE"
    }

    """ 带参数调用人脸检测 """
    data = __client.detect(image, image_type, options)
    return data['result']['face_list']


if __name__ == '__main__':
    print(detect('001.jpg'))
