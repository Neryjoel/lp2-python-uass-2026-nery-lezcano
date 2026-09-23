from funciones import *

# programa principal
num = int(input("Número a procesar (0 para salir): "))
while num != 0:
    print("Suma:", suma_digitos(num))
    num = int(input("Número a procesar (0 para salir): "))
