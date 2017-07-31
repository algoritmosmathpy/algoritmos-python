import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.sqrt(x + 2)

x = np.array([4, 8, 0, 6, 2, -2]) #Crear vector valores de x

y = f(x)

#Tabla de los valores de la funcion
tabla = pd.DataFrame(list(zip(x, y)), columns=['x', 'f(x)'])
print(tabla)

def move_spines():
    """Esta funcion divide pone al eje y en el valor 
    0 de x para dividir claramente los valores positivos y
    negativos."""
    fix, ax = plt.subplots()
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_position("zero")
    
    for spine in ["right", "top"]:
        ax.spines[spine].set_color("none")
    
    return ax

x = np.linspace(-2, 6, num=30)

ax = move_spines()
ax.grid()
ax.plot(x, f(x))
plt.title(r"Grafico de $f(x)=\sqrt{x+2}$")
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()