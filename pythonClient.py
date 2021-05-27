
import socket

port = 2500
address = ("localhost", port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
while TRUE:
    msg = input("Message to send: ")
    s.send(msg.encode()) #send a message to server
    r_msg = s.resc(BUFSIZE) #recieve message from server
    if not r_msg:break
    print("Received message: %s" %r_msg.decode())
