"""
Este algoritmo nos ayudara a calcular la hipotenusa de un triangulo rectangulo, simplemente pasandole los valores de los 2 catetos.

Para este algoritmo se usara el Teorema de Pitágoras

Teorema de Pitágoras:

En todo triángulo rectángulo el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos.
"""

#Importamos la libreria Math para usar su metodo sqrt.
import math

#Le pedimos al usuario los 2 catetos
cateto1 = float(input("Introducir el Primer cateto: "))
cateto2 = float(input("Introducir el Segundo cateto: "))

#En una variable almacenamos el resultado
#Como dice el teorema de pitagoras, el cuadrado de la hipotenusa sera la raiz cuadrada de cateto1**2 + cateto2**2
hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))

print("Hipotenusa: ", hipotenusa)