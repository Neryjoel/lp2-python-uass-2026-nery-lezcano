from funciones import *

# programa principal
cantidad = 0
num = int(input("Número (-1 para cortar): "))
while num != -1:
    print("Factorial:", factorial(num))
    cantidad += 1
    num = int(input("Número (-1 para cortar): "))

print("Se leyeron", cantidad, "números")
