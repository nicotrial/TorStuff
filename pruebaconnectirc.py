import socket
import socks
import sys
import ssl
import time
from threading import Thread



channel = "#channel"
botnick = "anon"
timeout = 30

			
def getServiceSSL(address,port):
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
	s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
	#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(timeout)
	try:
		result = s.connect((address,port))
		sock = ssl.wrap_socket(s)
		print("[*]Connected Sending Data")
		sock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" "+ botnick +"\n")
		sock.send("NICK "+ botnick +"\n")
		#sock.send("PRIVMSG nickserv :iNOOPE\r\n")
		#sock.send("LIST\n")
		#sock.send("JOIN "+ channel +"\n") 
		print("[*]Send complete")
		recvSubProcess = Thread(target=getReponse, args=(sock,))
		recvSubProcess.start()
		#recvSubProcess.join()
		time.sleep(5)
		#sock.send("LIST\n")
		#time.sleep(2)
		#sock.send("NAMES #hacking\n")
		datatosend = str(input("INPUT:"))
		while "!q" not in datatosend:
			datatosend = str(input("INPUT:"))
			sock.send(datatosend+"\n")
		recvSubProcess.stop()
		sock.close()
	except Exception as e:
		print("[!]Error connectiong to port "+str(port)+" of "+address + " :::::")
		print e
		
def getService(address,port):
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
	s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
	#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(timeout)
	try:
		result = s.connect((address,port))
		print("[*]Connected Sending Data")
		s.send("USER "+ botnick +" "+ botnick +" "+ botnick +" "+ botnick +"\n")
		s.send("NICK "+ botnick +"\n")
		#sock.send("PRIVMSG nickserv :iNOOPE\r\n")
		#sock.send("LIST\n")
		#sock.send("JOIN "+ channel +"\n") 
		print("[*]Send complete")
		recvSubProcess = Thread(target=getReponse, args=(s,))
		recvSubProcess.start()
		#recvSubProcess.join()
		datatosend = input("ANYKEY TO KILL ")
		s.close()
	except Exception as e:
		print("[!]Error connectiong to port "+str(port)+" of "+address)

		
def getReponse(sock):
	while True:
			data=sock.recv(4096)
			#print("[*]DataREcieved")
			sys.stdout.write(data)
			if data.find("PING") != -1:
				sock.send("PONG " + data.split() [1] + "\r\n")



if __name__ == "__main__":
	if sys.argv[1]:
		if len(sys.argv) > 3:
			if sys.argv[3] == "ssl":
				getServiceSSL(sys.argv[1],int(sys.argv[2]))
			else:
				print("BRAHHH WTF ARE U SAYING?????? ")
		else:
			getService(sys.argv[1],int(sys.argv[2]))
	print("[*]DONE ")