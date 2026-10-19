#Desafio extra - registro de votos

def cargar_votos():
    votos = {}
    print("Escriba el candidato por el que vota (Enter solo para terminar)")

    while True:
        nombre = input("Voto: ").capitalize()

        #si no escribio nada se termina la votacion
        if nombre == "":
            break

    #si ya esta en el diccionario le sumo 1, si no lo creo con 1
        if nombre in votos:
            votos[nombre] += 1
        else:
            votos[nombre] = 1

    return votos


def contar_total(votos):
    total = 0
    for nombre in votos:
        total += votos[nombre]
    return total


def buscar_ganador(votos):
    #se va guardando al que tenga mas votos hasta ahora
    ganador = ""
    mas_votos = 0

    for nombre in votos:
        if votos[nombre] > mas_votos:
            mas_votos = votos[nombre]
            ganador = nombre

    #si hay empate queda el que se cargo primero
    return ganador


#Programa principal
votos = cargar_votos()

if len(votos) == 0:
    print("No hubo votos")
else:
    print("\n--- Votos por candidato ---")
    for nombre in votos:
        print(nombre + ":", votos[nombre])

    print("\nGanador:", buscar_ganador(votos))
    print("Total de votos:", contar_total(votos))