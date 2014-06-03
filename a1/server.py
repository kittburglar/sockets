#import socket library
from random import randint
from socket import * 
#set port to 12000
serverPort = 12000
#create server socket 
print 'Setting up TCP Socket'
serverSocket = socket(AF_INET,SOCK_STREAM) 
#make server listen to port 12000
serverSocket.bind(('',serverPort)) 
serverSocket.listen(1) 
print 'SERVER_PORT={}'.format(serverPort)
#wait for a connetion to client
while 1: 
 connectionSocket, addr = serverSocket.accept() 
 #store client's string into a buffer
 sentence = connectionSocket.recv(1024)
 
 if int(sentence) == 13:
   r_port = randint(1420,11000)
   print 'Negotiation accepted, sending r_port',r_port
   serverPort = r_port
   connectionSocket.send(str(r_port))
   print 'Setting up UDP socket'
   serverSocket2 = socket(AF_INET, SOCK_DGRAM)
   serverSocket2.bind(('', serverPort))
   sentence, clientAddress = serverSocket2.recvfrom(2048) 
   print 'Reversing message...'
   reversedMessage = sentence[::-1]
   #send it back to client through socket 
   print 'Message sent.'
   serverSocket2.sendto(reversedMessage, clientAddress)
 connectionSocket.close()   
