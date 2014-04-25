#!/usr/bin/env python3

import socket

HOST=""
PORT=8888

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

data = client.recv(1024)
print(data.decode())

client.send("Hello Server!".encode())

client.close()
