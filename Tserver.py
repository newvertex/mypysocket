#!/usr/bin/env python3

import socket
import threading

HOST=""
PORT=8855

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

def serv():
	while True:
		conn, addr = server.accept()
		print(addr)
		conn.send("Hello Client!".encode())
		clients.append(conn)
		threading.Thread(target=usr, args=(conn,)).start()
	server.close()

def usr(conn):
	while True:
		data = conn.recv(1024)
		print(data.decode())
		for client in clients:
			client.send("# ".encode()+data)
	conn.close()

if __name__ = '__main__':
	serv()

