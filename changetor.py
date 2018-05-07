import socket
import time
import requests

proxies = {
    'http': 'socks5://localhost:9150',
    'https': 'socks5://localhost:9150'
}

session = requests.Session()
session.proxies = {'http': 'socks5://127.0.0.1:9150', 'https': 'socks5://127.0.0.1:9150'}

tor_c = socket.create_connection(("127.0.0.1",  9151))
for x in range(0, 5):
	tor_c.send(b'AUTHENTICATE "poronga"\r\nSIGNAL NEWNYM\r\n')
	time.sleep(10)
	print(session.get("http://icanhazip.com").text)
tor_c.close()