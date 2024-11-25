#Galilea Peralta Contreras.
#25 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python

#Conjunto vacio
nombres = set()

print(f"Conjunto vacio: {nombres}")

nombres.add("Rebeca")
nombres.add("Juan")
nombres.add("Bryan")
nombres.add("Jamilete")
nombres.add("Galilea")
nombres.add("Rosalinda")
nombres.add("Jenny")
nombres.add("Tania")
nombres.add("Juan")
nombres.add("Hector")

print(nombres)


nombres.remove("Tania")

for nombre in nombres:
    print(nombre,end = " ")
print()
print(f"El elemento Galilea pertene al conjunto ? { "Galilea" in nombres}")

#Nuevo conjunto de números
Cojunto_de_numeros = set()

Cojunto_de_numeros = {12,1,12,3,2,-2,3,11,1}

#Funciones basicas
Tamaño_de_conjunto = len(Cojunto_de_numeros)
Suma_de_conjunto = sum(Cojunto_de_numeros)

print(f"La suma de todos los elementos son: {Suma_de_conjunto}")