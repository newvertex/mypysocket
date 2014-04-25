#!/usr/bin/env python3

import socket, threading

HOST=""
PORT=8855

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def recv():
	while True:
		data = client.recv(1024)
		print(data.decode())

def send():
	while True:
		msg = input(": ")
		client.send(msg.encode())

if __name__ == '__main__':
	threading.Thread(target=recv).start()
	send()
