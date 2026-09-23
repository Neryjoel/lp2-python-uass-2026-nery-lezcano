from funciones import *

# Consigna: sin ejecutar el programa, determinar la salida si x=6, y=7.
# Respuesta: 9 . 10
# (coordenada_z usa copias locales de x, y: no modifica las variables
# globales del programa principal, por eso el resultado de la función
# se descarta y solo importan los incrementos x=x+1 / y=y+1 del bucle)

# programa principal
x = int(input("Coordenada eje x: "))
y = int(input("Coordenada eje y: "))
for i in range(3):
    z = coordenada_z(x, y)
    x = x + 1
    y = y + 1
print(x, " . ", y)
