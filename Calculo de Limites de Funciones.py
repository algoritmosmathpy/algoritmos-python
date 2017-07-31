from sympy.interactive import printing
from sympy import limit, Symbol, S

# imprimir con notación matemática.
printing.init_printing(use_latex='mathjax') 

#Esta sera nuestra funcion, la cual calcularemos el limite
def f(x):
	return x**2 - x + 2

x = Symbol('x') #Creando el simbolo x

result = limit(f(x), x, 2) #Creamos el objeto limit, nos dara directamente el resultado
print("Resutado de x**2 - x + 2, cuando x tiende a 2: " ,result) #Mostramos el resultado, el cual sera, 4

"""
También podemos calcular los Límites de valores de x que tiendan hacia el infinito utilizando la clase especial S.Infinity que nos proporciona SymPy
"""

# Resolviendo limite 1/x cuando x tiende a infinito
result2 = limit(1/x, x, S.Infinity)
print("Resultado de 1/x, cuando x tiende hacia el infinito: ",result2)
