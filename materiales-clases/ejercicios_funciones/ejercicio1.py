from funciones import *

# programa principal
direccion = input("Tu email: ")
if validar_email(direccion):
    print("Dirección válida")
else:
    print("Dirección inválida")
