import os
import threading
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=input("Enter your IP = ")
port=8002
s.bind((ip,port))

sender_ip=input("Enter sender IP =")
sender_port=8001
os.system('tput setaf 6')
print('\t\t\t\t\t\t')
os.system('figlet "Chatting App " -f bubble')

def send():
	while True:
		os.system('tput setaf 2')
		message=input().encode()
		s.sendto(message,(sender_ip,sender_port))
		if message.decode()=='exit' :
			os._exit(1)
			
def receive():
	while True:
		os.system('tput setaf 3')
		message=s.recvfrom(1000) 
		if message[0].decode()=='exit' :
			os.exit(1)

		print("\n\t\t\t\t\t\t\t\t\t\t\tReceived  -  "+message[0].decode()+"\n")
		
thread1= threading.Thread(target=send)
thread2= threading.Thread(target=receive)

thread1.start()
thread2.start()

			
