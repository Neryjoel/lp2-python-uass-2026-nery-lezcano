from funciones import *

# programa principal
mayor = 0
numero = int(input("Número primo: "))
while es_primo(numero):
    print("Suma de los dígitos:", suma_digitos(numero))
    digito = int(input("Dígito: "))
    print("El", digito, "aparece", frecuencia(numero, digito), "veces")
    if numero > mayor:
        mayor = numero
    numero = int(input("Número primo: "))

print("Factorial de", mayor, ":", factorial(mayor))
