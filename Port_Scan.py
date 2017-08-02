import socket
import subprocess
import sys
from datetime import time

remote_server = input("Host Remoto: ")
remoteServerIp = socket.gethostbyname(remote_server)

try:
	for port in range(1,80):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIp, port))
		if result == 0:
			print("Port {}:	  open").format(port)
		sock.close()
except KeyboardInterrupt:
	sys.exit()

except socket.gaierror:
	sys.exit()

except socket.error:
	sys.exit()

print("Escaneo completado")