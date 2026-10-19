#Ejercicio 8 - inventario
inventario = {
    "Teclado": 10,
    "Mouse": 5,
    "Monitor": 2
}


def pedir_cantidad():
    # isdigit() dice si lo que escribieron son solo numeros
    texto = input("Cantidad: ")
    if not texto.isdigit():
        print("Tiene que ser un numero entero..")
        return 0
    cant = int(texto)
    if cant <= 0:
        print("La cantidad debe ser mayor a 0")
        return 0
    return cant


def agregar_stock():
    producto = input("Producto: ").title()
    if producto not in inventario:
        print("Ese producto no esta en el inventario")
        return
    cant = pedir_cantidad()
    if cant > 0:
        inventario[producto] += cant
        print("Listo, ahora hay", inventario[producto], "de", producto)


def vender_producto():
    producto = input("Producto a vender: ").title()
    if producto not in inventario:
        print("Ese producto no esta en el inventario")
        return
    cant = pedir_cantidad()
    if cant == 0:
        return
    # no se puede vender mas de lo que hay
    if cant > inventario[producto]:
        print("No alcanza el stock, quedan", inventario[producto])
    else:
        inventario[producto] -= cant
        print("Venta registrada, quedan", inventario[producto])


def consultar_stock():
    producto = input("Producto a consultar: ").title()
    if producto in inventario:
        print(f"{producto}: {inventario[producto]} unidades")
    else:
        print("Ese producto no esta en el inventario")


#programa principal
while True:
    print("\n--- INVENTARIO ---")
    print("1. Agregar stock")
    print("2. Vender producto")
    print("3. Consultar stock")
    print("4. Salir")

    op = input("Opcion: ")

    if op == "1":
        agregar_stock()
    elif op == "2":
        vender_producto()
    elif op == "3":
        consultar_stock()
    elif op == "4":
        print("Chau")
        break
    else:
        print("Opcion invalida")