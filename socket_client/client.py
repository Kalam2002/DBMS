import socket
victim_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_ip = '10.0.2.5'
server_port = 7777

while(True) :
	msg = input("Enter message : ")
	victim_socket.sendto(msg.encode(), (server_ip, server_port))
	
