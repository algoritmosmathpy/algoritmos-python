"""
Programa que abre un servidor HTTP en el puerto 8000, que muestra un mensaje.
"""

#Importamos las siguienetes librerias
from http.server import HTTPServer, BaseHTTPRequestHandler

#Creamos una clase que heredara los metodos de BaseHTPPRequestHandler
class serverHTTP(BaseHTTPRequestHandler):
	def do_GET(self):
		#Enviamos una respuesta al servidor, en este caso 200 (OK)
		self.send_response(200)

		#Enviamos las Cabezeras, el contenido del documento sera HTML
		self.send_header('Content-type', 'text/HTML; charset=utf-8')
		self.end_headers()

		#Variable que contendra el mensaje que mostraremos en el servidor en formato HTML
		self.mensaje = "<h1>Hola MathPy!!!</h1>"

		#Escribimos en el documento del servidor
		self.wfile.write(self.mensaje.encode())

if __name__ == '__main__':
	server_address = ((''), 8000)
	httpd = HTTPServer(server_address, serverHTTP)
	print("El servidor esta abierto en el puerto 8000, dirigete a http://localhost:8000/")
	httpd.serve_forever()



