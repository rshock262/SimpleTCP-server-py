#import socket module

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Prepare server socket

#####Fill in start####
ip = socket.gethostbyname(socket.gethostname())
port = 8080
addr = (ip, port)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(addr)
serverSocket.listen(1)
#####fill in end####

while True:
    #establish connection
    print 'Ready to serve at ', ip, ':', port
    connectionSocket, addr = serverSocket.accept()
    print 'Connection from ',addr
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        ####Fill in start####
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
        ####fill in end####
        #send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
    except IOError:
        #send response message for file not found
        ####Fill in start
        connectionSocket.send('File not found')
        ####fill in end
        
        #close client socket
        ####fill in start
        connectionSocket.close()
        ####fill in end
    except IndexError:
        connectionSocket.send('No file requested')
    finally:
        connectionSocket.close()

        
serverSocket.close()
