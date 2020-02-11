import socket

SRV_ADDR = input('What is the server ip: ')
SRV_PORT = input('Which port Range (ex 3-45): ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SRV_PORT_L = int(SRV_PORT.split('-')[0])
SRV_PORT_H = int(SRV_PORT.split('-')[1])

for port in range(SRV_PORT_L, SRV_PORT_H):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status= s.connect_ex((SRV_ADDR, port))
    if (status == 0):
        print('Port: ',port,'is UP')
    else:
        print('Port: ',port,'is DOWN')
        s.close()
