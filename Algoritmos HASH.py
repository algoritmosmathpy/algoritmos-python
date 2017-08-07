"""
Algoritmo para codificar el texto "Hola mundo" en distintos codigos Hash en su forma hexodecimal.

Algunos algoritmos hash son: MD5, sha1, sha256, sha224, entre otros.
"""

#importamos la libreria hashlib
import hashlib as hl 

#Creamos un for para  recorrer todos los algoritmos hash disponibles
for algoritmos in hl.algorithms_available:
	#Codificamos la cadena "Hola Mundo" (Si quieres puedes cambiear el texto), y pedimos que su salida sea hexodecimal
	h = hl.new(algoritmos, b'Hola mundo').hexdigest()
	#Mostramos los resultados
	print(algoritmos, ":")
	#Mostramos el texto codificado
	print(h)
	print("\n")