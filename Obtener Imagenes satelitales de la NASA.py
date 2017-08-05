"""
Este pequeño programa nos permitira conectarnos a la API de la NASA para poder obtener imagenes satelitales.

En este ejemplo se utiliza una DEMO_KEY, con el cual se podran hacer una cuantas llamadas a la api, si quieres crear algun tipo de proyecto 
te recomiendo que te dirijas al sitio https://api.nasa.gov/index.html#apply-for-an-api-key para obtener una Key API

Estar atetos en dinde este su script ya que hay sera donde se descargue la imagen.
"""

#Importamos la libreria Requests para hacer peticiones a servidores
import requests
import webbrowser
#Le pedimos al usuario que introduzca una fecha con el formato Año-Mes-Dia
date = input("introduzca una fecha con el formato Año-Mes-Dia (Ej: 2008-04-05): ")
#Parametros que le pasaremos a la peticion
params = {'api_key':'DEMO_KEY',
			#Date es la fecha de la imagen que nos devolvera el servidor la cual descargaremos
			'date': date}
print("Obteniendo imagen satelital de la fecha ", params['date'])
#Creamos una conección con los servidores de la NASA
response = requests.get('https://api.nasa.gov/planetary/apod?', params=params)
#Obtenemos la respuesta del servidor en un formato json
responseJSON = response.json()
#En ocasiones en vez de darnos una imagen nos dan un video
#Por ello comprobaremos que la respuesta sea una imagen
#Si la respuesta no es una imagen se nos abrira una pestaña en nuestro navegador con el link del video
if responseJSON['media_type'] == "image":
	#Enviamos una peticion a la url que nos devuelve https://api.nasa.gov/planetary/apod?
	responseIMG = requests.get(responseJSON['url'])
	#Luego iteramos la respuesta y le escribimos en un fchero de formato jpg con escritura Binaria
	with open('apod-'+params['date']+'.jpg', 'wb') as img:
		for x in responseIMG.iter_content():
			img.write(x)
		print("\n Imagen apod-"+params['date']+".jpg descargado correctamente.")
		img.close()
#Como ya mencione si la respuesta no es una imagen se abrira una pestaña en nuestro navegado con el video
#Si quieres puedes hacer lo mismo que lo de la imagen, descargar el video, simplemente repite el procedimiento de arriba
else:
	webbrowser.opne_new_tab(responseJSON['url'])
