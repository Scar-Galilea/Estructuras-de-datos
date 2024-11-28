#Galilea Peralta Contreras.
#26 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.

print("*** Conjunto de números ***")
Conjunto_A = set()
Conjunto_B = set()

Conjunto_A = {11,7,10,9,5,1,15,7}
Conjunto_B = {55,70,11,77,66,9,5}

#Operaciones basicas
Union = Conjunto_A | Conjunto_B
print(Union)
print()
Interseccion = Conjunto_A & Conjunto_B
print(Interseccion)
print()
print("*** Conjunto de animales  ***")
Lista_original = ["Leon","Leopardo","Aguila","Gato","Chapulin","Venaro","Leopardo","Gato"]
print(Lista_original)
print()

Conjunto_de_animales = set(Lista_original)
print(Conjunto_de_animales)
lista_modificada = list(Conjunto_de_animales)
print(lista_modificada)
Tupla_de_animales = tuple(Lista_original)
print(Tupla_de_animales)


# Se crean dos conjuntos de números.
print("Se crean dos conjuntos.")

conjuntoA = {2, 223, 12, 1, 3, 4, 1, 6}    # Notar que el conjunto intenta repetir 2 veces el no. 1.
conjuntoB = {12, 23, 0, 6, 30, 4, 10}

print(f"Conjunto A: {conjuntoA}")
print(f"Conjunto B: {conjuntoB}")
print()

# Operaciones básicas.
print("Operaciones básicas.")

union = conjuntoA | conjuntoB
print(f"Unión de los conjuntos (|): {union}")   # La unión omite los valores repetidos en ambos conjuntos.

interseccion = conjuntoA & conjuntoB
print(f"Intersección de los conjuntos (&): {interseccion}") # Son los valores que coinciden en ambos conjuntos.

diferencia = conjuntoA - conjuntoB
print(f"Resta de los conjuntos: {diferencia}")  # Son los valores del conjunto A menos los que coincidente con el conjunto B.
print()

# Convertir de lista a conjunto y viceversa.
print("Convertir de lista a conjunto y viceversa.")

lista = ["Perro", "Gato", "Ratón", "Cuyo", "Gato", "Lobo", "Perro"]
print(f"Lista original: {lista}")

conjunto = set(lista)
print(f"Lista como conjunto: {conjunto}")      # No considera los valores repetidos.

lista_reconvertida = list(conjunto)
print(f"Lista reconvertida del conjunto: {lista_reconvertida}")
