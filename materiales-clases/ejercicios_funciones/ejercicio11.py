from funciones import *

# programa principal (demo de la función dni_valido)
dni = int(input("DNI: "))
if dni_valido(dni):
    print("DNI válido")
else:
    print("DNI inválido")
