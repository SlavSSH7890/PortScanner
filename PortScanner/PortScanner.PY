#portscanner or whatever this is.

from http import client

import socket
import sys


target_host = "example.com"         #change website domain URL
target_port = 443                    #change to any legal port number
ipv4user = socket.inet_aton("1.1.1.1")        #---- legal IPv4 address (most likely not affected - in this space of portscanner)

#create the stream or TCP connection of anykind
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#do not leave it hanging for a long time.
client.settimeout(1)                           #set a timeout of 1 second to avoid hanging or many prints in the termenial (limitation)



valideHOSTSresult = client.connect_ex((target_host, target_port))

if valideHOSTSresult == 0: #0 means that the connection was successful
    print(f"Host {target_host} is reachable on port {target_port}")
else:
    print(f"Host {target_host} is not reachable on port {target_port}")
client.close()
