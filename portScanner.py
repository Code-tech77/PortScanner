import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Timeout seconds
s.settimeout(3)

#input IP address
host = input("Please Enter the IP you want to scan : ")
#input port
port = int(input("Please Enter the port you want to scan: "))

#Message user
def portScanner(port):
    if s.connect_ex((host, port)):
        print("Port is closed")
    else:
        print("Port is open")
        
portScanner(port)
