"""
Algoritmo que implementa la formula de Bhaskara para resolver ecuaciones cuadraticas (de segundo grado)

Ejercicio: encuentra los dos valores para resolver la siguiente ecuacion, 7x**2 + 3x - 4 = 0

"""

#Importamos la librera math para usar el metodo sqrt
import math

#Pedimos la entrade de los tres valores de la ecuacio, a = cociente del termino cuadratico, b = cociente de termino lineal y c = termino independiente
a = float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))
c = float(input("Ingrese el valor de C: "))

#Como nos dice la formula, restamos el valor de b elevado a la 2, con el valode de 4 * a * c
x = (b**2)-(4*a*c)

#Si x es menor que 0, no tendra una solucion dentro de las reglas de los numeros reales
if x < 0:
    print("Solucion solo en numeros complejos")
elif x == 0:
    x1 = (-b) / (2*a)
    print("%.2f" % x1)
else:
	#Luego sumamos o restamos (nos dara 2 valores diferentes, pero ambos igualaran la ecuacion)
	#sumamos el valor de -b a la raiz cuadrada de x y luego lo dividimos entre 2 * a
    x1 = (-b + math.sqrt(x)) / (2*a)
    x2 = (-b - math.sqrt(x)) / (2*a)

    #Mostramos ambos valores
    print("X1: ", x1)
    print("X2: ", x2)