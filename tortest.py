#need to install tor and run with python2
#apt-get install tor
#service tor start
#torsocks curl icanhazip.com


import socket
import socks
import http.client
import urllib2
import time
import base64
import codecs
import random

def recv_timeout(the_socket,timeout=1):
	the_socket.setblocking(0)
	total_data=[];
	data='';
     
	#beginning time
	begin=time.time()
	while 1:
		#if you got some data, then break after timeout
		if total_data and time.time()-begin > timeout:
			break
         
		#if you got no data at all, wait a little longer, twice the timeout
		elif time.time()-begin > timeout*2:
			break
         
		#recv something
		try:
			data = the_socket.recv(8192)
			if data:
				total_data.append(data)
 				#change the beginning time for measurement
				begin=time.time()
		except:
			pass
     
	#join all parts to make final string
	return ''.join(total_data)

def generateRSAKey():
	key = base64.b32encode(codecs.decode(codecs.encode('{0:020x}'.format(random.getrandbits(80))),'hex_codec')).lower()
	print (key)
	return key

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
sock = socks.socksocket()
sock.settimeout(10)
#print (dir(sock))		
newkey = generateRSAKey()
print("new connection")
try:	
	sock.connect(('3dbr5t4pygahedms.onion', 80))
	#sock.connect((newkey + '.onion', 80))
	message = 'GET /info.php\r\n\r\n'
	sock.sendall(message)
	print(recv_timeout(sock))
except:
	pass	
sock.close()
#time.sleep(1)

