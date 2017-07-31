"""
Problema:

Se deja caer de lo alto de un edifico una pelota que tarda 3 segundo en tocar el suelo

Calcular:
1)Con que velocidad la pelota toca el piso
2)Altura del Edificio
"""

import math

#Valores con los que contamos
Vo = 0
t = 3
g = 9.8

#Calcular la velocidad final
Vf = Vo + (g*t)

#Calcular la altura del Edificio
y = (Vo * t) + (g*t**2 / 2)

print("Velocidad Final: ", Vf)
print("Altura del Edificio: ", y)