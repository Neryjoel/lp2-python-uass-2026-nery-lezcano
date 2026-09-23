from funciones import *

# programa principal
sumatoria = 0
num = int(input("Número a procesar (0 para salir): "))
while num != 0:
    print("Suma:", suma_digitos(num))
    sumatoria += num
    num = int(input("Número a procesar (0 para salir): "))

print("Sumatoria:", sumatoria)
print("Dígitos de la sumatoria:", suma_digitos(sumatoria))
