import socket
import threading
from colored import fg

# creating a socket
# AF_INET : Address family IPv4
# SOCK_DGRAM : Connectionless Protocol i.e UDP (User Datagram Protocol)
s= socket.socket( socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter your IP: ")
port = int(input( "Enter port no.: "))

# binding the port/address to the socket 
s.bind(( ip, port ))

ip_server= input(" Enter server side IP: ")
port_server= int(input(" Enter port no."))
dis_msg="Chat-app"
print("\n"+"{:^10}".format(dis_msg)+"\n")
def receive():
    while True:
        response=s.recvfrom(1024)     
        mssg_server= response[0].decode()   # Message from server in "string format"
        color = fg('green')
        if(mssg_server!=None):
        	print (color+"\n"+"server "+ " : " + mssg_server )
        color = fg('yellow')

def send():
    while True:
        color = fg('yellow')
        input_msg=input("\n"+color+"{:>15}".format("You")+" : ")
        if(input_msg!=None):
        	s.sendto( input_msg.encode(), ( ip_server, port_server ))
        color = fg('green')
        
    

# applying multithreading
thread1= threading.Thread( target= send )
thread2= threading.Thread( target= receive)
thread1.start()
thread2.start()