
# Ejercicio 1 - guardar 5 productos en productos.txt
def ejercicio_1():
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        for i in range(5):
            nombre = input(f"Producto {i + 1}: ")
            precio = input("Precio: ")
            archivo.write(nombre + " - " + precio + "\n")

    print("Productos guardados en productos.txt")


#ejercicio 2 - leer productos.txt
def ejercicio_2():
    with open("productos.txt", "r", encoding="utf-8") as f:
        for linea in f:
            # el strip saca el salto de linea del final
            print(linea.strip())


#ejercicio 3 - agregar nombre y edad a registro.txt (modo append)
def ejercicio_3():
    nombre = input("Nombre: ")
    edad = input("Edad: ")

    # 'a' = escribe al final sin borrar lo anterior
    with open("registro.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} - {edad}\n")

    print("Listo, se agrego al registro")


#Ejercicio 4 - promedio de numeros.txt -> resultado.txt
def ejercicio_4():
    suma = 0
    cantidad = 0

    with open("numeros.txt", "r", encoding="utf-8") as entrada:
        for linea in entrada:
            linea = linea.strip()
            if linea != "":          # por si hay lineas vacias
                suma += float(linea)
                cantidad += 1

    if cantidad > 0:
        promedio = suma / cantidad
    else:
        promedio = 0

    with open("resultado.txt", "w", encoding="utf-8") as salida:
        salida.write("Promedio: " + str(promedio))

    print("Promedio:", promedio)


#ejercicio 5 - copiar origen.txt a destino.txt
def ejercicio_5():
    with open("origen.txt", "r", encoding="utf-8") as origen:
        with open("destino.txt", "w", encoding="utf-8") as destino:
            for linea in origen:
                destino.write(linea)

    print("Archivo copiado")


#Programa principal
while True:
    print("\n--- MANEJO DE ARCHIVOS ---")
    print("1. Guardar productos")
    print("2. Mostrar productos")
    print("3. Agregar al registro")
    print("4. Calcular promedio")
    print("5. Copiar archivo")
    print("6. Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        ejercicio_1()
    elif opcion == "2":
        ejercicio_2()
    elif opcion == "3":
        ejercicio_3()
    elif opcion == "4":
        ejercicio_4()
    elif opcion == "5":
        ejercicio_5()
    elif opcion == "6":
        break
    else:
        print("Opcion invalida")