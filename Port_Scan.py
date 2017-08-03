"""
Algoritmo que detecta puertos abiertos en un Host Remoto
"""

#Importamos las librerias
import socket
import subprocess
import sys
from datetime import time

#Le pedimos al usuario que nos proporcione el Host Remoto
remote_server = input("Host Remoto: ")
#Obtenemos la ip del Host
remoteServerIp = socket.gethostbyname(remote_server)

try:
	for port in range(1,80):
		#Creamos una conexion con el Host
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIp, port))
		if result == 0:
			#Imprimimos los puertos abiertos	
			print("Port {}:	  Abierto").format(port)
		sock.close()
except KeyboardInterrupt:
	sys.exit()

except socket.gaierror:
	sys.exit()

except socket.error:
	sys.exit()

print("Escaneo completado")