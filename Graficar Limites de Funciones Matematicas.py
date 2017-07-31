import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

def f(x):
	return x**2 - x + 2

x = np.array([1, 1.5, 1.9, 1.95, 1.99, 1.999, 2.001, 2.05, 2.1, 2.2, 2.5, 3])
y = f(x)
tabla = pd.DataFrame(list(zip()), colums=['x', 'f(x)'])
print(tabla)

def move_spines():
    fix, ax = plt.subplots()
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_position("zero")
    
    for spine in ["right", "top"]:
        ax.spines[spine].set_color("none")
    
    return ax

x = np.linspace(-2, 4, num=30)
ax = move_spines()
ax.grid()
ax.plot(x, f(x))
ax.scatter(2, 4, lable="Limite cuando x tiende a 2", color='r')
plt.legend()
plt.title(r"Grafico de $f(x)=x^2 -x +2$")
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()