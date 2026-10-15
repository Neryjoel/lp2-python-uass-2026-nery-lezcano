#Ejercicio 3 - Eliminar duplicados
def eliminar_duplicados(lista):
    return set(lista)


#Programa principal
numeros = [1, 2, 2, 3, 3, 3, 4]
resultado = eliminar_duplicados(numeros)
print(resultado)