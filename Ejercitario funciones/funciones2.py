# #Ejercicio 2
# def buscar(lista, valor):
#     for nombre in lista:
#         if nombre == valor:
#             return True
#     return False


# #Programa principal
# alumnos = ["Ana", "Luis", "Carlos", "Pedro", "Maria Luisa", "César"]

# if buscar(alumnos, "Maria Luisa"):
#     print("Maria Luisa está en la lista")
# else:
#     print("Maria Luisa no está en la lista")


#profe Ejercicio 2
def buscar(lista, valor):
    for nombre in lista:
        if nombre == valor:
            return True
        return False


#Programa principal
alumnos = ["Ana", "Luis", "Carlos", "Pedro", "Maria Luisa", "César"]
nombre = input('Ingrese el nombre a buscar: ')
resultado = buscar(alumnos, nombre)
print(resultado)