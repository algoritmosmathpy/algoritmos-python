"""
Algoritmo para hacer una Busqueda Binaria  de un dato dentro de un vector

El algoritmo toma como entrada un entero, luego el algoritmo procesa esa entrada y verificara si ese entero se encuentra dentro del vector

Visita nuestra pagina web, para ver más algoritmos: algoritmosmathpy.github.io/algoritmosmathpy/
"""

#Este es el vector que el algoritmo usara para buscar cualquier dato
vector = [8, 3, 5, 9, 10, 22, 45, 500, 455, 900, 4253]
#Los Datos dentro del vector deben estar ordenados, de lo contrario algunos valores no seran encontrados
#Para eos, usamos el metodo sort, que nos permite ordenar el vector de manera acendente
vector.sort()
#La variable puntero sera el inicio del vector, que es 0
puntero = 0
#vectorLen contiene la longitud del vector
vectorLen = len(vector)
#La varieable encontrado cambiara su valor, y asi el algoritmo sabre que hacer luego
encontrado = False

#Le pedimos al usuario una entrada de un entero
numero = int(input("Ingresar un numero: "))

#Creamos un bucle que no se detenga hasta que encontrado sea diferente de False
#Y que puntero sea menor o igual que vectroLen
while not(encontrado) and puntero <= vectorLen:
	#Creamos la variable mitad
	mitad = int((puntero+vectorLen) / 2)
	#Si numero es igual que el indice mitad en vector
	if numero == vector[mitad]:
		#Encontado sera igual a True
		encontrado = True
	#De lo contrario, si el indice mitad en vector es menor que numero
	elif numero < vector[mitad]:
		#vectorLen sera igual que mitad - 1
		vectorLen = mitad - 1
	#De lo conteario
	else:
		#Puntero sera igual que mitad + 1
		puntero = mitad + 1
#Si encontrado es True
if(encontrado):
	#MOstramos un mensaje con la posicion del Dato en el vector
	print("El dato se encuentra en la posicion ", str(mitad+1))
	#Mostramos el vector ordenado
	print(vector)
#De lo contrario
else:
	#Mostramos un mensaje avisandole al usuario que el dato ingresado no se encuentra dentro del vector
	print("El dato no se encontro")
