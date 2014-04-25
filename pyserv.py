#!/usr/bin/env python3

import socket

HOST=""
PORT=8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

conn, addr = server.accept()
print(addr)

conn.send("Hello client!".encode())

data = conn.recv(1024)
print(data.decode())

conn.close()
server.close()
