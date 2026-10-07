# # manejo de archivos en python

# # Manejo manual - Apertura y cierre manuales

# #archivo = open("C:\\lp2-python-uass-2026-nery-lezcano\\Archivos\\datos.txt", "r", encoding="utf-8") # modo lectura
# archivo = open("C:/lp2-python-uass-2026-nery-lezcano/Archivos/datos.txt", "r", encoding="utf-8") # modo lectura

# contenido = archivo.read() # leer todo el contenido del archivo

# archivo.close() # cerrar el archivo , se puede usar with open() para que se cierre automáticamente

# print(contenido) # imprimir el contenido del archivo


#2_

# with open("C:/lp2-python-uass-2026-nery-lezcano/Archivos/datos.txt", "r", encoding="utf-8") as archivo: # modo lectura
#     contenido = archivo.read() # leer todo el contenido del archivo
#     print(contenido) # imprimir el contenido del archivo
#     #se cierra automáticamente al salir, no necesita archivo.close()


# with open("C:/lp2-python-uass-2026-nery-lezcano/Archivos/datos.txt", "r", encoding="utf-8") as archivo: # modo lectura
#     contenido = archivo.readline() # leer una línea del archivo
#     print(contenido) # imprimir el contenido del archivo
#     #se cierra automáticamente al salir, no necesita archivo.close()

# with open("C:/lp2-python-uass-2026-nery-lezcano/Archivos/datos.txt", "r", encoding="utf-8") as archivo: # modo lectura
#     contenido = archivo.readlines() # leer todas las líneas del archivo
#     print(contenido) # imprimir el contenido del archivo
#     #se cierra automáticamente al salir, no necesita archivo.close()

#3_

# #Iterar el archivo con FOR lee linea por línea, igual que readline() pero de forma mas simple
# with open("C:/lp2-python-uass-2026-nery-lezcano/Archivos/datos.txt", "r", encoding="utf-8") as archivo: # modo lectura
#     for linea in archivo:
#         print(linea) # imprimir el contenido del archivo
#         #se cierra automáticamente al salir, no necesita archivo.close()

# #Iterar el archivo con FOR lee linea por línea, igual que readline() pero de forma mas simple
# with open("C:/lp2-python-uass-2026-nery-lezcano/Archivos/datos.txt", "r", encoding="utf-8") as archivo: # modo lectura
#     for linea in archivo:
#         print(linea.strip()) # imprimir el contenido del archivo
#         #O end="" evita que se agregue un salto de línea adicional al final de cada línea, ya que print() agrega un salto de línea por defecto.
#         print(linea, end="")
#         #se cierra automáticamente al salir, no necesita archivo.close()

#4

with open("C:/lp2-python-uass-2026-nery-lezcano/Archivos/notas.txt", "w", encoding="utf-8") as archivo: # modo escritura
    archivo.write("Hola mundo\n") # escribir en el archivo
    archivo.write("Esta es una línea de texto\n") # escribir en el archivo
    archivo.write("Esta es otra línea de texto\n") # escribir en el archivo
    archivo.write("Esta es la última línea de texto\n") # escribir en el archivo
    #se cierra automáticamente al salir, no necesita archivo.close()

    #for alumno in ["Juan", "Pedro", "María", "Ana"]:
    
    for alumno in range(4): # iterar 4 veces
        alumno = input("Ingrese el nombre del alumno: ") # pedir al usuario que ingrese el nombre del alumno

        archivo.write(alumno + "\n") # escribir en el archivo
        nota = input(f"Ingrese la nota de {alumno}: ") # pedir al usuario que ingrese la nota del alumno
        archivo.write(f"{alumno}: {nota}\n") # escribir en el archivo