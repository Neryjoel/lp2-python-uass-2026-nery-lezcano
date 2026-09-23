from funciones import *

# Consigna: el programa debería imprimir 2 con x=5, y=1, pero imprime 5.
# Corrección: maximo/minimo usaban las variables globales x, y en vez de
# sus propios parámetros a, b. Ya están corregidas en funciones.py.

# programa principal
x = int(input("Un número: "))
y = int(input("Otro número: "))
print(maximo(x - 3, minimo(x + 2, y - 5)))
