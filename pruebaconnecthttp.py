import socket
import socks
import sys

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


			
def getService(address,port):
	sock = socks.socksocket()
	sock.settimeout(10)
	try:
		result = sock.connect((address,port))
		sock.send('GET / HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: keep-alive\r\nAccept: text/html\r\nUser-Agent: YoMama\r\n\r\n'.encode(encoding='utf-8'))
		try:
			response = sock.recv(1024)
			print("----------------"+address+"----------------------")
			print(response)
			print("-------------------------------------------------")
		except Exception as e:
			print("Error in request of "+address)
		sock.close()
	except Exception as e:
		print("Error connectiong to port "+str(port)+" of "+address)
		

if __name__ == "__main__":
	if sys.argv[1]:
		getService(sys.argv[1],int(sys.argv[2]))
	print("DONE ")