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
