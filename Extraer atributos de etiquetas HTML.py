"""
Algoritmo para extraer atributos de las etiquetas HTML de una pagina determinada

Al ejecutar le algoritmo tendras que pasarle 3 entradas:
1)URL de la Pagina, muy importante colocar la url con el protocolo https o http (Ejemplo: https://facebook.com)
2)Etiqueta de la cual se extraera el valor del atributo (Ejemplo: img)
3)Atributo que se extraera de la etiqueta (Ejemplo: src)

En este caso se podria extraer todos los Link de las imagenes de facebook.
"""

#Importamos las librerias necesarias
import queue
import urllib.request
import re
from urllib.parse import urljoin
 
#Pediamos al usuario que nos proporciona la url de la pagina
url = input("URL de la Pagina: ")

#Le enviamos una peticion al servidor
def descargar(pagina):
    try:
        peticion = urllib.request.Request(pagina)  
        html = urllib.request.urlopen(peticion).read()
        print("Descarga OK: ", pagina)
    except:
        print('Error descargando',pagina)
        return None
        
    return html
    
 #Desntro del HTML que nos devolvio el servidor extraemos el contenido de los atributos
def rastrearEnlaces(pagina):
    etiqueta = input("Nombre de la Etiqueta: ")
    atributo = input("Nombre del Atributo: ")
    buscaEnlaces = re.compile('<'+etiqueta+'[^>]+'+atributo+'=["'"](.*?)["'"]', re.IGNORECASE)
    cola = queue.Queue()
    cola.put(pagina) 
    visitados = [pagina]
    print("Buscando atributo "+atributo+" en la etiqueta "+etiqueta+" dentro de la pagina",pagina)
    while (cola.qsize() > 0):
        html = descargar(cola.get())
        if html == None:
            continue
        enlaces = buscaEnlaces.findall(str(html))
        for enlace in enlaces:
            enlace = urljoin(pagina, str(enlace))
            if(enlace not in visitados):
                cola.put(enlace)
                visitados.append(enlace)
 

if __name__ == "__main__":           
    rastrearEnlaces(url)