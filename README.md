# SimpleTCP-server-py
Dead simple TCP server in python for an old class project
Basic program execution:
The python program (TCP-Simple-Server.py) is the TCP web server. To run it, use python 2.7, it will start a TCP connection by listing your local IP address, and the port it is on. Using an internet browser type the IP address followed by the port number (8080) and the html file (hello.html)
Ex: http://192.168.1.101:8080/hello.html
This should display an html page, and at the same time the python window should display a message about the new connection with your IP address and a random port number your computer will automatically assign.  
	Ex: Connection from (‘192.168.1.101’, 57438)
To close the program, hit Ctrl and C on the python code window, this will break the loop the code uses to continue to establish connections. Refresh your browser window and the python code will close, the html page now will not load as the connection has been broken.
