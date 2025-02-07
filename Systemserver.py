import socket
# Create a socket obj
s = socket.socket()
#bind the socket with the port number
s.bind(('127.0.0.1', 2040))
# listening for a request
s.listen()
# accept the connection
mySocket,clientSocket=s.accept()
print("Connection established with: "+ str(clientSocket))

while True:
    # Sending data to the client
    msg=input('Server:')
    mySocket.send(bytes(msg, 'utf-8'))
    if msg=='bye':
        break;
    # Receiving data from the client
    data=mySocket.recv(1024)
    print('Client:'+ data.decode('utf-8'))


mySocket.close()