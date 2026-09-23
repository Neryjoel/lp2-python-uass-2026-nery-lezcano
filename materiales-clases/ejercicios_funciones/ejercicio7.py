from funciones import *

# programa principal
cantidad = 0
mayor = -1
n_mayorsuma = None
numero = int(input("Número positivo (-1 para cortar): "))
while numero != -1:
    suma = suma_digitos(numero)
    if suma > mayor:
        mayor = suma
        n_mayorsuma = numero
    if suma < 10:
        cantidad += 1
    numero = int(input("Número positivo (-1 para cortar): "))

print("Sumatoria de dígitos de", n_mayorsuma, ":", mayor)
print("Cantidad con sumatoria menor a 10:", cantidad)
