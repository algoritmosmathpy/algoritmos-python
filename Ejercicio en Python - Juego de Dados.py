"""
Programa que simula un juego de dados usando la libreria random
"""

#Importamos la libreria random
import random
print("** JUEGO DE AZAR CON DADOS**")
#Creamos una varable llamada dinero
dinero = 0
#Le pedimos al usuario la entrada de un entero que en este caso sera el numero de intents
intentos = int(input("Ingrese cantidad de intentos:  "))
#Creamos un bucle for 
for i in range(intentos):
    #Creamos nuestro dado
    dado = random.randint(1,6)
    #Si el dado es igual a 6, ganaras $4
    if dado == 6:
        dinero=dinero+4
        print("Dado = 6, Ha ganado $4")
    #Si el dado es igual a 3, ganaras $1
    elif dado==3:
        dinero=dinero+1
        print("Dado = 3, Ha ganado $1")
    #Si el dado es igual a 1, no ganaras ni perderas dinero.
    elif dado==1:
        print("Siga participanto")
    #Si el dado es igual a 2, 4 0 5, perderas $2
    elif dado==2 or dado==4 or dado==5:
        dinero=dinero-2
        print("Pierde $2 ")
#Mostramos tu dinero actual
print("Ganancia Total: $", dinero)
