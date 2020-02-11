import socket

SRV_ADDR = input("Type the server ip address: ")
SRV_PORT = int(input("Which port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)

print("Server Start! Waiting for connections....")
connection, address = s.accept()

print("Client connect eith address: ", address)

while 1:
    data = connection.recv(1024)
    if not data : break
    connection.sendall(b'-- Message Received --\n')
    print(data.decode('utf-8'))
connection.close()
