#ejercicio 9 - Ranking de alumnos
def mejor_alumno(alumnos):
    mejor = alumnos[0]

    for alumno in alumnos:
        if alumno[1] > mejor[1]:
            mejor = alumno

    return mejor


def peor_alumno(alumnos):
    peor = alumnos[0]

    for alumno in alumnos:
        if alumno[1] < peor[1]:
            peor = alumno

    return peor


def promedio_general(alumnos):
    suma = 0

    for alumno in alumnos:
        suma += alumno[1]

    return suma / len(alumnos)


#Programa principal
alumnos = [
    ("Juan", 85),
    ("Ana", 95),
    ("Pedro", 70)
]

nombre, nota = mejor_alumno(alumnos)
print(f'Mejor alumno: {nombre} ({nota})')

nombre, nota = peor_alumno(alumnos)
print(f'Peor alumno: {nombre} ({nota})')

print(f'Promedio general: {promedio_general(alumnos):.2f}')
