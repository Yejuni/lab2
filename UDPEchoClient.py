#!/usr/bin/python3

import socket
server_IP='203.250.133.88'
server_port=10109
BUFF_SIZE= 1024


sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#server_address = (host,port)
#sock.bind(server_address)

server_addr=(server_IP,server_port)
message = input("Enter message : ")
#message = bytes(message,encoding = 'utf-8')

try:

        byte_sent= sock.sendto(message.encode(),server_addr)
        data,address = sock.recvfrom(BUFF_SIZE)
        print("Received from server: {}".format(data.decode()))

except Exception as e :
    print("Exception : %s" %str(e))

sock.close