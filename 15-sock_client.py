#!/usr/bin/env python3

import socket

# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(('127.0.0.1', 9999))

# 从服务器接收欢迎消息
print(s.recv(1024).decode('utf-8'))

# 向服务器发送数据
for data in [b'Micheal', b'Tracy', b'Jason']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close


