import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 12345)) #if the clients/server are on different network you shall bind to ('', port)

s.listen(10)
c, addr = s.accept()
print('{} connected.'.format(addr))

f = open("voiture.jpg", "rb")
l = os.path.getsize("voiture.jpg")
m = f.read(l)
c.sendall(m)
f.close()
print("Done sending...")