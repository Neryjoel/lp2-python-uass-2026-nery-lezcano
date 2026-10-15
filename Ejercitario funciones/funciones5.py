#Ejercicio 5 - Promedio de notas
def calcular_promedio(notas):
    promedio = sum(notas)/len(notas)
    return promedio

def estado(promedio):
    if promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"


#Programa principal
notas = [70, 80, 90, 60]
promedio = calcular_promedio(notas)
resultado = estado(promedio)

print(f'El promedio del alumno es {promedio}')
print(f'El estado del alumno es {resultado}')