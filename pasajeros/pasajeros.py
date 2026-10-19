
# Gestion de pasajeros

#lista con los datos de los pasajeros
pasajeros = [
    ("Manuel Juarez", 19823451, "Liverpool"),
    ("Silvana Paredes", 22709128, "Buenos Aires"),
    ("Rosa Ortiz", 15123978, "Glasgow"),
    ("Luciana Hernandez", 38981374, "Lisboa")
]

# ciudades y sus Paises
ciudades = [
    ("Buenos Aires", "Argentina"),
    ("Glasgow", "Escocia"),
    ("Lisboa", "Portugal"),
    ("Liverpool", "Inglaterra"),
    ("Madrid", "España")
]


#Busca si existe el DNI
def buscar_pasajero(dni):
    for p in pasajeros:
        if p[1] == dni:
            return p
    return None


#ver de que pais es la ciudad
def buscar_pais(ciudad):
    for c in ciudades:
        if c[0].lower() == ciudad.lower():
            return c[1]
    return None


def agregar_pasajero():
    nombre = input("Nombre: ")
    dni = int(input("DNI: "))
    destino = input("Destino: ")

    #comprobar los datos antes de agregar
    if buscar_pasajero(dni) is not None:
        print("El DNI ya existe")
    elif buscar_pais(destino) is None:
        print("La ciudad no existe")
    else:
        pasajeros.append((nombre, dni, destino))
        print("Pasajero agregado")


# Agregar una nueva ciudad ala lista
def agregar_ciudad():
    ciudad = input("Ciudad: ")
    pais = input("Pais: ")

    if buscar_pais(ciudad) is not None:
        print("La ciudad ya existe")
    else:
        ciudades.append((ciudad, pais))
        print("Ciudad agregada")


#consultar el destino usando el DNI
def ver_ciudad():
    dni = int(input("DNI: "))
    p = buscar_pasajero(dni)

    if p is None:
        print("Pasajero no encontrado")
    else:
        print(p[0], "viaja a", p[2])


def contar_ciudad():
    ciudad = input("Ciudad: ")
    cantidad = 0

    #contar los que viajan a esa ciudad
    for p in pasajeros:
        if p[2].lower() == ciudad.lower():
            cantidad += 1

    print("Cantidad de pasajeros:", cantidad)


def ver_pais():
    dni = int(input("DNI: "))
    p = buscar_pasajero(dni)

    if p is None:
        print("Pasajero no encontrado")
    else:
        pais = buscar_pais(p[2])
        print(p[0], "viaja a", pais)


#contar cuantos pasajeros van a un pais
def contar_pais():
    pais = input("Pais: ")
    cantidad = 0

    for p in pasajeros:
        destino = buscar_pais(p[2])

        if destino is not None and destino.lower() == pais.lower():
            cantidad += 1

    print("Cantidad de pasajeros:", cantidad)


#menu principal
while True:
    print("\n--- Gestion de pasajeros ---")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Ver ciudad de un pasajero")
    print("4. Contar pasajeros por ciudad")
    print("5. Ver pais de un pasajero")
    print("6. Contar pasajeros por pais")
    print("7. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        agregar_pasajero()
    elif opcion == "2":
        agregar_ciudad()
    elif opcion == "3":
        ver_ciudad()
    elif opcion == "4":
        contar_ciudad()
    elif opcion == "5":
        ver_pais()
    elif opcion == "6":
        contar_pais()
    elif opcion == "7":
        print("Hasta luego")
        break
    else:
        print("Opcion incorrecta")
