import socket
import threading
from colored import fg

# creating a socket
# AF_INET : Address familt IPv4
# SOCK_DGRAM : Connectionless Protocol i.e UDP (User Datagram Protocol)
s= socket.socket( socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter server side IP: ")
port = int(input( "Enter port no. : "))
# binding the port/address to the socket 
s.bind(( ip, port ))
dis_msg="Chat-app"
print("\n"+"{:^10}".format(dis_msg)+"\n")
def receive():
    global ip_client, port_client
    while True:
        response=s.recvfrom(1024)     
        ip_client= response[1][0]           # IP of client
        port_client= response[1][1]
        mssg_client= response[0].decode()   # Message from client in "string format"
        color = fg('green')
        if(mssg_client!=None):
        	print (color+"\n"+"client "+ " : " + mssg_client )
        color = fg('yellow')
      

def send():
    while True:
        color = fg('yellow')
        input_msg=input(color+"\n"+"{:>15}".format("You")+" : ")
        if(input_msg!=None):
        	s.sendto( input_msg.encode(), ( ip_client, port_client ))
        color = fg('green')
        


# applying multithreading
thread1= threading.Thread( target= send )
thread2= threading.Thread( target= receive )
thread1.start()
thread2.start()