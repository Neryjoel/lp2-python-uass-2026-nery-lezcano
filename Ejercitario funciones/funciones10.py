#Ejercicio 10 - gestion de estudiantes
estudiantes = {
    "Juan": [70, 80, 90],
    "Ana": [100, 95, 90]
}


def agregar_estudiante():
    nombre = input("Nombre del estudiante: ").title()

    if nombre == "":
        print("No escribiste ningun nombre")
        return
    if nombre in estudiantes:
        print("Ese estudiante ya esta cargado")
        return

    notas = []
    print("Ingrese las notas (escriba 'fin' para terminar)")
    while True:
        dato = input("Nota: ")
        if dato == "fin":
            break
        #valido que sea numero y que este entre 0 y 100
        if not dato.isdigit():
            print("Eso no es una nota..")
            continue
        nota = int(dato)
        if nota > 100:
            print("La nota va de 0 a 100")
            continue
        notas.append(nota)

    if len(notas) == 0:
        print("No se cargaron notas, no se agrega el estudiante")
        return

    estudiantes[nombre] = notas
    print("Estudiante agregado")


def calcular_promedio(notas):
    return sum(notas) / len(notas)


def mostrar_promedios():
    if not estudiantes:
        print("Todavia no hay estudiantes")
        return
    for nombre in estudiantes:
        prom = calcular_promedio(estudiantes[nombre])
        print(f"{nombre} -> {prom:.2f}")


def mejor_estudiante():
    if not estudiantes:
        print("Todavia no hay estudiantes")
        return
    mejor = ""
    mejor_prom = 0
    for nombre in estudiantes:
        prom = calcular_promedio(estudiantes[nombre])
        if prom > mejor_prom:
            mejor_prom = prom
            mejor = nombre
    print(f"El mejor es {mejor} con {mejor_prom:.2f}")


#Programa principal
while True:
    print("\n1. Agregar estudiante")
    print("2. Mostrar promedios")
    print("3. Mostrar mejor estudiante")
    print("4. Salir")

    opcion = input("Elija una opcion: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_promedios()
    elif opcion == "3":
        mejor_estudiante()
    elif opcion == "4":
        break
    else:
        print("Opcion invalida")