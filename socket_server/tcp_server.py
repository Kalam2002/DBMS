import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 9999))
server_socket.listen(1)
print("Waiting for client..")

conn, addr = server_socket.accept()
print(f"Connection from {addr}")

while True :
	data = conn.recv(1024)
	if not data : 
		break
	print(f"Client: {data.decode()}")
	conn.sendall(b"ACK: " + data)
