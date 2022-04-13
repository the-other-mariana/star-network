# udp_receiver.py

import socket
port = 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("", port))

print"UDP server: waiting for client on port ", port, "..."
cnt = 1

while 1:
	data, address = server_socket.recvfrom(256)
	print cnt, "( " ,address[0], " " , address[1] , " ) "
	cnt = cnt + 1

