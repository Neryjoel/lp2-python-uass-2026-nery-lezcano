# #iterar mediante ciclos FOR
# #Iteracr sobre una lista
# #lenguajes = ["Python", "Java", "C++", "JavaScript",'PHP']
# # for elemento in lenguajes:
# #     print(elemento)


# # #iNSTRUCCIONES PARA MODIFICAR EL FLUJO DE UNA CICLO FOR
# # #Haremos que el ciclo se rompa con la primera usando break
# # for elemento in lenguajes:
# #     if elemento == "C++":
# #         break
# #     print(elemento)


# #Romper el ciclo actual si el elemento es igual a "C++"
# for elemento in lenguajes:
#     if elemento == "PHP":
#         break
#     print(elemento)
# #ELIMNAR EL ELEMENTO "C++" DE LA LISTA


#Pasar al siguiente elemeento de la lista cuando se cumpla una condición usando continue
# lenguajes = ["Python", "Java", "C++", "JavaScript",'PHP']

# for elemento in lenguajes:
#     if elemento == "C++" or elemento == "PHP":
#         continue #saltarse ese elemeto y pasar al siguiente
#     print(elemento)

#iterar sobre una cadena de caracteres
# for letra in "Python":
#     print(letra)



# #iterar sobre numeros consecutivos usando la función range() start,stop,step
# for numero in range(5): #0,1,2,3,4
#     print(numero)

# for numero in range(1, 51): #1,2,3,...,50
#     print(numero)

# for numero in range(1, 51, 2): #1,3,5,...,49
#     print(numero)



# #Disminuir el valor de aumento del rango(por defecto es 1) 
# for numero in range(200,2,-2): #200,198,196,...,4,2
#     print(numero)

# #en reversa
# for numero in reversed(range(1, 51)): #50,49,48,...,2,1
#     print(numero)

# #otra forma de iterar sobre listas usando indices
# lenguajes = ["Python", "Java", "C++", "JavaScript",'PHP']
# for index in range(len(lenguajes)):
#     print(f"El lenguaje en la posición {index} es: {lenguajes[index]}")







# Ejemplo 1: sumar todos los números de una lista
# numeros = [1, 2, 3, 4, 5]
# suma = 0
# for numero in numeros:
#     suma += numero
# print(f"La suma de los números es: {suma}")

#ejemplos 2: encontrar el numero más grande en una lista
# numeros = [10, 5, 8, 20, 15]
# maximo = numeros[0] #posicion 0
# for numero in numeros:
#     if numero > maximo:
#         maximo = numero
# print(f"El número más grande es: {maximo}")

# #Ejemplo 3:  contar las vocales en una cadena de carecteres
# cadena = "Hola, ¿cómo estás?"
# vocales = "aeiouAEIOU"
# contador = 0
# for letra in cadena:
#     if letra in vocales:
#         contador += 1
#         print(f"Se encontró la vocal: {letra}")
# print(f"El número de vocales es: {contador}")

# #Ejemplo 4: imprimir una tabla de multiplicar
# numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
# print(f"Tabla de multiplicar del {numero}:")
# for i in range(1, 11):
#     print(f"{numero} x {i} = {numero * i}")

#ejemplo 5: generar una lista de los primeros 10 números cuadrados
# cuadrados = []
# for i in range(1, 11):# de 1 al 10
#     cuadrados.append(i ** 2)#este append agrega el valor al final de la lista
# print("Los primeros 10 números cuadrados son:", cuadrados)


#ejemplo 6: invertir una cadena de caracteres
# cadena = input("Ingrese una cadena de caracteres: ")
# cadena_1 = cadena[::-1] #otra forma de invertir una cadena
# print("La cadena invertida es:", cadena_1)
# cadena_invertida = ""
# for letra in cadena:
#     cadena_invertida = letra + cadena_invertida #agrega la letra al inicio de la cadena invertida
# print("La cadena invertida es:", cadena_invertida)

#ejemplo 7: filtrar numeros pares de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)#esto hace que se agregue el numero par a la lista numeros_pares
print("Los números pares son:", numeros_pares)