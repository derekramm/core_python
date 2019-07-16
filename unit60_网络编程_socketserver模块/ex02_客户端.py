#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_客户端.py"""

import socket
ip_port = ('127.0.0.1', 5884)
sk = socket.socket()
sk.connect(ip_port)
server_data = sk.recv(1024).decode()
print('服务器:', server_data)
while True:
    inp = input('请输入消息:').strip()
    sk.sendall(inp.encode())

    if inp == 'exit':
        print("谢谢使用，再见！")
        break

    server_data = sk.recv(1024).decode()
    print('服务器:', server_data)

sk.close()
