# Client
import socket
s=socket.socket()
s.bind(('127.0.0.1',3000))
s.connect(('127.0.0.1',2040))
while True:
    # receiving data from server
    msg=s.recv(1024)
    print('Server:'+msg.decode('utf-8'))
    if msg.decode('utf-8')=='bye':
        break;
    # Sending data to server
    data=input('Client:')
    s.send(bytes(data,'utf-8'))

s.close()