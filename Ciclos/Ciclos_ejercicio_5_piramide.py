#Galilea Peralta Contreras.
#07 de noviembre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
#Para poder usar el ciclo while se utiliza de la siguiente manera (falta mas).

Numero_de_filas = int(input("Ingrese el número de filas: "))

for j in range (1,Numero_de_filas + 1):
    asteriscos = "*" * j
    print(f"{asteriscos}")
    j += 1

print()

for i in range (1,Numero_de_filas + 1):
    i = Numero_de_filas
    asteriscos = "*" * i
    print(f"{asteriscos}")
    i -= 1


