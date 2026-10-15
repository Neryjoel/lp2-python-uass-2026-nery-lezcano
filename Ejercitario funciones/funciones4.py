#Ejercicio 4 - Frecuencia de elementos
def contar_frecuencia(lista):
    frecuencia = {}

    for elemento in lista:
        #Consultar si el elemento ya está en el diccionario o no
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1

    return frecuencia


#Programa principal
lista = ["a", "b", "a", "c", "a", "b"]
print(contar_frecuencia(lista))