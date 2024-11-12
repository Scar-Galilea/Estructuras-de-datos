#Galilea Peralta Contreras.
#12 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python

#lista va con corchetes
#una lista es dordenado y mutable
#Ordenado significa que cada cosa  tiene un orden especifico
#Mutable es que cambia

#Crear lista
"""
Alumnos = []
Alumnos.append("Hector")
Alumnos.append("Addi")
Alumnos.append("Alberto")
Alumnos.append("Juan")

print(Alumnos)
print(Alumnos[1])

print()
Alumnos.insert(1,"Tania")
print(Alumnos[1])
print()
for Alumno in Alumnos:
    print(Alumno,end = " ")

Alumnos.remove("Hector")
print(Alumnos)

Alumnos.pop(2)
print(Alumnos)

del Alumnos[2]
print(Alumnos)

"""

Grupo = []
Grupo.append("Rebeca")
Grupo.append ("Juan")
Grupo.append("Bryan")
Grupo.append("Duran")
Grupo.append ("Hector")
Grupo.append ("Tania")
Grupo.append ("Jennifer")
Grupo.append ("Rosalinda")
Grupo.append ("Galilea")
Grupo.append ( "Patricia")
Grupo.append ("Addi")
Grupo.append( "Alberto")

print(Grupo)

len(Grupo)
print(Grupo)
print()

Grupo.sort()
print(Grupo)
print()

Grupo.sort(reverse = True)
print(Grupo)
print()

print(Grupo[11])
