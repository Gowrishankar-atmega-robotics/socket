import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname('www.atmegarobotics.tech.blog')
print(ip)
