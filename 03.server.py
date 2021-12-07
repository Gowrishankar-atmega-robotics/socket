import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 12347 
s.bind(('', port))
print("port binded to :",port)
s.listen(5)
print("socket is listening")
while True:
    c, addr = s.accept()
    print('Got connectiom from ', addr)
    c.send("thank you for connecting".encode())
    c.send("this is important msg".encode())
    c.close()
    break 