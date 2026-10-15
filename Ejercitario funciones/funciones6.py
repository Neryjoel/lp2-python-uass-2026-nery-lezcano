#Ejercicio 6 - Agenda telefónica

#Diccionario para agregar los contactos
agenda = {
    "Juan": "098111111",
    "Ana": "098222222"
}


#Funciones
def agregar_contacto():
    nombre = input('Ingrese el nombre: ')
    numero = input('Ingrese el número telefónico: ')

    agenda[nombre] = numero
    print('Contacto agregado correctamente..')


def buscar_contacto():
    nombre = input('Ingrese el nombre a buscar: ')
    if nombre in agenda:
        print(f'Teléfono de {nombre}: {agenda[nombre]}')
    else:
        print('Contacto no encontrado..')


def mostrar_contactos():
    if len(agenda) == 0:
        print('La agenda está vacía..')
    else:
        print('\n --- Contactos ---')
        for nombre, telefono in agenda.items():
            print(f'{nombre}: {telefono}')


#Programa principal
while True:
    print('\n === AGENDA TELEFÓNICA ===')
    print('1. Agregar contacto')
    print('2. Buscar contacto')
    print('3. Mostrar contactos')
    print('4. Salir')

    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        agregar_contacto()
    elif opcion == '2':
        buscar_contacto()
    elif opcion == '3':
        mostrar_contactos()
    elif opcion == '4':
        print('Hasta luego')
        break
    else:
        print('Opción no válida')