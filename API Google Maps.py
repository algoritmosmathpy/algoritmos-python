import socket
from urllib.parse import quote_plus
cabecera = """\
GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\r\n\
Host: maps.google.com:80\r\n\
User-Agent:  \r\n\
Connection: close\r\n\
\r\n\
"""
def localizar(direccion):
    conexion = socket.socket()
    conexion.connect(('maps.google.com', 80))
    cabeceraAux = cabecera.format(quote_plus(direccion))
    conexion.sendall(cabeceraAux.encode('utf-8'))
 
    datos = b''
    d = conexion.recv(1024)
    while d:
         datos += d
         d = conexion.recv(1024)
 
    print(datos.decode('utf-8'))
 
 
if __name__ == '__main__':
    address = input("Direccion: ")
    localizar(address)