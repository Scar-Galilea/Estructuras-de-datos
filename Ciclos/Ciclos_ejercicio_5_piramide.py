#Galilea Peralta Contreras.
#07 de noviembre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
#Para poder usar el ciclo while se utiliza de la siguiente manera (falta mas).

Numero_de_filas = int(input("Ingrese el número de filas: "))

for j in range (1,Numero_de_filas + 1):
    asteriscos = "*" * j
    print(f"{asteriscos}")

print()

contador = Numero_de_filas
for i in range (1,Numero_de_filas + 1):
    asteriscos = "*" * contador
    print(f"{asteriscos}")
    contador -= 1

print()
contador = Numero_de_filas
for k in range (1,Numero_de_filas + 1):
    espacio = " " * k
    asteriscos = "*" * contador
    print(f"{espacio}{asteriscos}")
    contador -= 1

print()
contador = Numero_de_filas
contador_2 = 0
for m in range (1,Numero_de_filas + 1):
    espacio = " " * contador
    asteriscos = "*" * (m + contador_2)
    print(f"{espacio}{asteriscos}")
    contador -= 1
    contador_2 += 1


