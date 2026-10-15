# #Ejercicio 1 - Estadisticas de una lista
# def estadisticas(lista):
#     suma = sum(lista)
#     promedio = suma / len(lista)
#     minimo = min(lista)
#     maximo = max(lista)
#     return suma, promedio, minimo, maximo

# # sum() = suma los números.
# # min() = busca el número menor.
# # max() = busca el número mayor.
# # len() = cuenta cuántos elementos hay.


# # Programa principal
# numeros = [10, 20, 30, 40, 50]
# suma, promedio, minimo, maximo = estadisticas(numeros)
# print("Suma:", suma)
# print("Promedio:", promedio)
# print("Mínimo:", minimo)
# print("Máximo:", maximo)

#como funciona el código promedio:
# sum(numeros) → suma los números: 150.
# len(numeros) → cuenta los números: 5.
# 150 / 5 → el promedio es 30.


#Profe ejercicio 1
#Ejercicio 1 - Estadísticas de una lista
def estadisticas(lista):
    maximo = 0
    minimo = lista[0]
    promedio = sum(lista)/len(lista)

    for numero in lista:
        #Si el valor de la posición actual es mayor al máximo, guardar éste valor
        if numero > maximo:
            maximo = numero

        if numero < minimo:
            minimo = numero
    
    return maximo, minimo, promedio

#Programa principal
numeros = [10, 20, 30, 40, 50]
mayor, menor, promedio = estadisticas(numeros)
print(f'El mayor es {mayor}, el menor es {menor} y el promedio es {promedio}')
