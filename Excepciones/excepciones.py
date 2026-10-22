# #Manejo de errores - excepciones
# #Ejemplo 1: ¿Qué pasa cuando no contemplamos el manejo de errores en nuestro código?
# numero = int(input("Ingrese un número: "))
# denominador = int(input("Ingrese un denominador: "))
# resultado = numero / denominador
# print("El número ingresado es:", numero)
# print("El denominador ingresado es:", denominador)
# print("El resultado es:", resultado)

# #Ajustamos la situacion anterior, para incluir el manjeo de errores, utilizando la estructura try-except
# #Ejemplo 2: Manejo de errores con try-except
# try:
#     numero = int(input("Ingrese un número: "))
#     denominador = int(input("Ingrese un denominador: "))
#     resultado = numero / denominador
#     print("El número ingresado es:", numero)
#     print("El denominador ingresado es:", denominador)
#     print("El resultado es:", resultado)
# except ValueError: #valores no numéricos
#     print("Error: Por favor, ingrese valores numéricos válidos.")
# except ZeroDivisionError: #denominador igual a cero
#     print("Error: El denominador no puede ser cero.")
# except Exception as e: #cualquier otro error
#     print("Ocurrió un error inesperado:", e)
# finally:
#     print("Fin del programa.")


#Ejemplo 2: Gestionar distintos tipos de errores
frutas = ['0-Piña', '1-Manzana', '2-Pomelo', '3-Naranja']

def elegir_fruta(lista_frutas):
    try:
        print(lista_frutas)
        indice = int(input('Elige una fruta mediante su número: '))
        print(f'Tu fruta favorita es {lista_frutas[indice]}')
    except IndexError:
        print(f'El índice es incorrecto, debe estar entre 0 y {len(lista_frutas)-1}')
    except ValueError:
        print('Error: debes ingresar un número entero.')
    except Exception as e:
        print('Ocurrió un error inesperado:', e)

elegir_fruta(frutas)

##Ejemplo 3: else, finally, raise
#vamos a s
cantidad = 0
while True:
    cantidad += 1
    try:
        total = 0
        sumandos = input('Ingrese algunos números, separados por espacios: ')
        sumandos = sumandos.split()
        print(sumandos)
        for num in sumandos:
            if num.isnumeric():# verifica si el valor es un número
                total += float(num)
            else:
                raise ValueError('El valor no es un número')
    except ValueError:
        print('Los valores son incorrectos..')
        print('Vuelva a introducir los números..')
    else:
        print(f'El valor de la suma es {total}')
        break
    finally:
        print('Esta es la iteración Nro: ', cantidad)
        print('Ha terminado el proceso..')