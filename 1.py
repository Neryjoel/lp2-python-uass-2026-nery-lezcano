# clave = 'contraseña'
# password = input('Ingrese la contraseña: ')
# if password.lower() == clave:
#     print('Acceso concedido')
# else:
#     print('Acceso denegado')

#2
# dividendo = float(input('Ingrese el dividendo: '))
# divisor = float(input('Ingrese el divisor: '))
# if divisor != 0:
#     cociente = dividendo // divisor
#     residuo = dividendo % divisor
#     print(f'El cociente es: {cociente}')
#     print(f'El residuo es: {residuo}')
# else:
#     print('Error: El divisor no puede ser cero.')

#3
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
numero = int(input('Ingrese un número entero: '))
if numero % 2 == 0:
    print(f'{numero} es un número par.')
else:
    print(f'{numero} es un número impar.')

