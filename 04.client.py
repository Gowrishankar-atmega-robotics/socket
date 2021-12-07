import socket
from time import sleep 
s = socket.socket()
port = 12347

s.connect(('127.0.0.1', port))
while True:
    print(s.recv(1024).decode())
    sleep(10)
    s.close()