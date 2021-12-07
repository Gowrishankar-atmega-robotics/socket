import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port  = 80

host_ip = socket.gethostbyname('www.atmegarobotics.tech.blog')

s.connect((host_ip, port))
print("connected success")
print(host_ip)