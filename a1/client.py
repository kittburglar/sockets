#Import socket library
import sys
from socket import * 
#Get user input and store it
serverName = str(sys.argv[1])
#Convert port input to int
serverPort = int(sys.argv[2]) 
#create socket
print 'Setting up TCP Socket...'
clientSocket = socket(AF_INET, SOCK_STREAM) 
#connect socket to stated servername and port
clientSocket.connect((serverName,serverPort)) 
sentence = str(sys.argv[3])
#send string to the server
print 'Negotiation with server'
clientSocket.send(str(13))

r_port, serverAddress = clientSocket.recvfrom(100)
print 'Recieved r_port:',r_port
serverPort = int(r_port)
print 'Setting up UDP Socket...'
clientSocket = socket(AF_INET, SOCK_DGRAM)
#store returned string from the server
print 'Sent message to server...' 
clientSocket.sendto(sentence,(serverName,serverPort))
modifiedSentence, serverAddress = clientSocket.recvfrom(1024) 
print 'From Server:', modifiedSentence
#close socket 
print 'Closing TCP Socket.'
clientSocket.close()

