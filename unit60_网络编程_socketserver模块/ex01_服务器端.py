#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_服务器端.py"""

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall('欢迎访问服务器！'.encode())
        while True:
            client_data = conn.recv(1024).decode()
            if client_data == "exit":
                print("断开与【%s】的连接！" % (self.client_address,))
                break
            print("来自【%s】的客户端向你发来信息：【%s】" % (self.client_address, client_data))
            conn.sendall(('已收到你的消息【%s】' % client_data).encode())

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 5884), MyServer)
    print("启动服务器！")
    server.serve_forever()
