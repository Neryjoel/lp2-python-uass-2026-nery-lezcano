"""
Funciones reutilizadas por los distintos ejercicios.
Se importan en cada programa principal con: from funciones import *
"""


def validar_email(email):
    """Retorna True si el email contiene '@'."""
    return "@" in email


def suma_digitos(numero):
    """Retorna la suma de los dígitos de un número entero."""
    numero = abs(numero)
    suma = 0
    while numero != 0:
        suma += numero % 10
        numero //= 10
    return suma


def es_primo(numero):
    """Retorna True si el número es primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def frecuencia(numero, digito):
    """Cuenta cuántas veces aparece 'digito' en 'numero'."""
    numero = abs(numero)
    cantidad = 0
    while numero != 0:
        if numero % 10 == digito:
            cantidad += 1
        numero //= 10
    return cantidad


def factorial(numero):
    """Retorna el factorial de un número entero no negativo."""
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado


def maximo(a, b):
    """Retorna el mayor entre a y b."""
    if a > b:
        return a
    return b


def minimo(a, b):
    """Retorna el menor entre a y b."""
    if a < b:
        return a
    return b


def coordenada_z(x, y):
    """Ejercicio 9: retorna x+10 más y+15 (usa copias locales de x, y)."""
    x = x + 10
    y = y + 15
    return x + y


def dni_valido(dni):
    """Retorna True si el DNI tiene 7 u 8 dígitos."""
    dni = abs(dni)
    cantidad = 0
    while dni != 0:
        cantidad += 1
        dni //= 10
    return cantidad == 7 or cantidad == 8


def longitud_ultima_palabra(cadena):
    """Retorna la longitud de la última palabra de una cadena."""
    palabras = cadena.split()
    if not palabras:
        return 0
    return len(palabras[-1])


def primeros_tres_digitos(numero):
    """Retorna los primeros 3 dígitos (de izquierda a derecha) de un número."""
    numero = abs(numero)
    while numero >= 1000:
        numero //= 10
    return numero


def obtener_identificador(nombre, dni):
    """Genera un identificador: primer nombre + cantidad de letras del
    apellido + primeros 3 dígitos del DNI."""
    nombre = nombre.strip()
    primer_nombre = nombre.split()[0]
    identificador = primer_nombre
    identificador += str(longitud_ultima_palabra(nombre))
    identificador += str(primeros_tres_digitos(dni))
    return identificador


def titulo(cadena):
    """
    Recibe una cadena y retorna una copia con la primera letra de cada
    palabra en mayúscula y el resto en minúscula.

    >>> titulo('esto es una frase')
    'Esto Es Una Frase'
    >>> titulo('ESTO ES UNA FRASE')
    'Esto Es Una Frase'
    >>> titulo('palabra')
    'Palabra'
    >>> titulo('   esto es una frase')
    '   Esto Es Una Frase'
    >>> titulo('esto es una frase   ')
    'Esto Es Una Frase   '
    >>> titulo('esto   es   una   frase')
    'Esto   Es   Una   Frase'
    >>> titulo('')
    ''
    >>> titulo(' ')
    ' '
    >>> titulo('123')
    '123'
    >>> titulo('-1esto 2es 3una 4frase')
    '-1Esto 2Es 3Una 4Frase'
    >>> titulo('esto1 es2 una3 frase4---')
    'Esto1 Es2 Una3 Frase4---'
    """
    nueva = ""
    inicio_palabra = True
    for caracter in cadena:
        if not caracter.isalpha():
            nueva += caracter
            inicio_palabra = True
        else:
            if inicio_palabra:
                nueva += caracter.upper()
                inicio_palabra = False
            else:
                nueva += caracter.lower()
    return nueva


if __name__ == "__main__":
    import doctest
    resultado = doctest.testmod()
    print(f"Doctests: {resultado.attempted - resultado.failed}/{resultado.attempted} OK")
