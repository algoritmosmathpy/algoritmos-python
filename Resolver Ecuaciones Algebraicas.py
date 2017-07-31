"""
Algortmos para resolver ecuaciones algebraicas

Todas las ecuaciones tienen que estar en su forma canonica, es decir, igual a cero

Ecuacion Algebraica: 2x - 6 + 2x = 6  - 5x + 9

Su forma canonica seria: 2x - 6 + 2x - 6 + 5x - 9 = 0

Este algoritmo tambien podra resolver eucaciones con 2 incognitas

"""

#Importamos la libreria sympy para usar variables simbolicas (x,y)
import sympy

sympy.init_printing()
#Pedimos al usuario que introduzca la ecuacion
ecuacion = input("Introducir ecuacion en su forma canonica: ")

#En una variable guardamos el resultado que nos dara el metodo solve
#El metodo solve toma 2 parametro, la ecuacion, y las variables simbolicas
result = sympy.solve([ecuacion], [x, y])

#Mostramos el resultado
print(result)
input()