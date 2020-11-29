#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("200.160.2.3",43))
s.send("globo.com\r\n")
resp = s.recv(1024)
print resp
