from funciones import *

# programa principal
nombre = input("Nombre del socio: ")
while nombre != "":
    dni = int(input("DNI del socio: "))
    while not dni_valido(dni):
        print("Número inválido.")
        dni = int(input("DNI del socio: "))
    print(obtener_identificador(nombre, dni))
    nombre = input("Nombre del socio: ")
