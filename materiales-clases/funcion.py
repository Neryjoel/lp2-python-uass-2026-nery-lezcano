# parametro->Nombre
#          ->tipo
#          ->valor(argumento)

# def Saludar():
#     print("Hola, Mundo?")
# Saludar()


# def Saludar(nombre):
#     print(f"Hola, {nombre}?")
# Saludar("Alice")

#ámbito de las variables
#1. Locales: definidas dentro de una función y solo pueden ser usadas dentro de esa función.
# def MiFuncion():
#     x = 10
#     print(x)

# def MiFuncion2():
#     print('Mi primer función')



#2. Globales: definidas fuera de una función y pueden ser usadas en cualquier parte
# apellido = "Lezcano"
# def MiFuncion3():
#     print('Mi primer función')
#     nombre = "Nery" # variable local
#     print(nombre, apellido)

# MiFuncion3()
# print(nombre) #esto no se puede hacer porque nombre es una variable local
# print(apellido)


#Parametros o argumentos de una funcion
#Creamos una funcion para calcular el perimetrio de un cuadrado (lado * 4)
#Formas de invocar a los parametros de una funcion
# def perimetro_cuadrado(lado, unidades):
#     perimetro = lado * 4
#     print("El perimetro es: ", perimetro, unidades) #esto no se puede hacer porque perimetro es una variable local
#     #1. Por orden/posicion (valor posicional)
# perimetro_cuadrado(5, "metros")

# #2. Por nombre (valor por nombre)
# perimetro_cuadrado(unidades="metros", lado=5)

# #3. Mezclando ambos (valor posicional y por nombre)
# perimetro_cuadrado(5, unidades="metros")


#Cuando necesitamos usar resultado de nuestras funciones en el proceso principal, debemos
#usar la instrucción return para devolver el resultado de la función al proceso principal.
# def perimetro_cuadrado(lado):
#     perimetro = lado * 4
#     return perimetro

# def area_cuadrado(lado):
#     area = lado * lado
#     return area


# #Podemos almacenar en una variable el resultado de la función
# perimetro = perimetro_cuadrado(5)
# area = area_cuadrado(5)
# print(f"El perimetro es: {perimetro}")
# print(f"El area es: {area}")


# #tambien, podemos retornar mas de una valor en la funcion
# def perimetro_area_cuadrado(lado):
#     perimetro = lado * 4
#     area = lado * lado
#     return perimetro, area

# perimetro, area = perimetro_area_cuadrado(5)
# print(f"El perimetro es: {perimetro}")


#funciones lambda: son funciones anonimas, es decir, no tienen nombre y se definen en una sola linea de codigo.
#Se definen con la palabra reservada lambda, seguida de los parametros, dos puntos y
#la expresion que se va a ejecutar.
#Ejemplo:
suma = lambda a, b: a + b
resta = lambda a, b: a - b
multiplicacion = lambda a, b: a * b
division = lambda a, b: a / b if b != 0 else "Error: División por cero"

print(suma(5, 3))
print(resta(5, 3))
print(multiplicacion(5, 3))
print(division(5, 3))