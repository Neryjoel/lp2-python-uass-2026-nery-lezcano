# Ejercicio 1: Control de acceso
print("EJERCICIO 1: CONTROL DE ACCESO")

edad = int(input("Ingrese su edad: "))
documento = input("¿Posee documento de identidad? (S/N): ").upper()

if edad >= 18 and documento == "S":
    print("Ingreso permitido.")
elif edad < 18:
    print("No puede ingresar porque es menor de edad.")
else:
    print("No puede ingresar porque no posee documento de identidad.")

# Ejercicio 2: Descuento en una tienda
print("\nEJERCICIO 2: DESCUENTO EN UNA TIENDA")

monto = float(input("Ingrese el monto de la compra: "))

if monto > 500000:
    porcentaje_descuento = 20
elif monto > 200000:
    porcentaje_descuento = 10
else:
    porcentaje_descuento = 0

descuento = monto * porcentaje_descuento / 100
total = monto - descuento

print("Monto original:", monto)
print("Descuento aplicado:", porcentaje_descuento, "%")
print("Total a pagar:", total)

# Ejercicio 3: Semáforo inteligente
print("\nEJERCICIO 3: SEMÁFORO INTELIGENTE")

color = input("Ingrese el color del semáforo: ").strip().lower()

if color == "verde":
    print("Avanzar")
elif color == "amarillo":
    print("Reducir velocidad")
elif color == "rojo":
    print("Detenerse")
else:
    print("Error: color no válido.")


# Ejercicio 4: Nivel de batería
print("\nEJERCICIO 4: NIVEL DE BATERÍA")

bateria = int(input("Ingrese el porcentaje de batería: "))

if bateria < 0 or bateria > 100:
    print("Error: el porcentaje debe estar entre 0 y 100.")
elif bateria <= 10:
    print("Batería crítica")
elif bateria <= 30:
    print("Batería baja")
elif bateria <= 80:
    print("Batería normal")
else:
    print("Batería alta")


# Ejercicio 5: Evaluación climática
print("\nEJERCICIO 5: EVALUACIÓN CLIMÁTICA")

temperatura = float(input("Ingrese la temperatura actual en °C: "))

if temperatura < 10:
    print("Mucho frío")
elif temperatura <= 24:
    print("Templado")
elif temperatura <= 34:
    print("Caluroso")
else:
    print("Muy caluroso")