import socket

SRV_ADDR = input('What is the server ip: ')
SRV_PORT = int(input('Which port: '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((SRV_ADDR, SRV_PORT))

while 1:
    user_input = input()
    user_input = SRV_ADDR +": "+ user_input
    s.sendall(user_input.encode())
    data = s.recv(1024)
    print(data.decode('utf-8'))
connection.close()

