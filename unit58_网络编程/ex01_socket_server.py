#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_socket_server.py"""

# !/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
ip_port = ('127.0.0.1', 9999)

sk = socket.socket()  # 创建套接字
sk.bind(ip_port)  # 绑定服务地址
sk.listen(5)  # 监听连接请求
print('启动socket服务，等待客户端连接...')
conn, address = sk.accept()  # 等待连接，此处自动阻塞
while True:  # 一个死循环，直到客户端发送‘exit’的信号，才关闭连接
    client_data = conn.recv(1024).decode()  # 接收信息
    if client_data == "exit":  # 判断是否退出连接
        exit("通信结束")
    print("来自%s的客户端向你发来信息：%s" % (address, client_data))
    conn.sendall('服务器已经收到你的信息'.encode())  # 回馈信息给客户端
conn.close()  # 关闭连接

