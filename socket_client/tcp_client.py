import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("10.0.2.5", 9999))

while True : 
	msg = input("Send : ")
	client_socket.send(msg.encode())
	response = client_socket.recv(1024)
	print(f"Server : {response.decode()}")
