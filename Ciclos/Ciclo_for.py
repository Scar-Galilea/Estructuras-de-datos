#Galilea Peralta Contreras.
#06 de noviembre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
#Para poder usar el ciclo while se utiliza de la siguiente manera (falta mas).

"""
sixtansis
for variable in secuencia
Toma todo lo que esta en secuencia

"""

#cada caracter es una cadena individual
Contador_de_caracteres = 0

cadena = input("Ingrese un nombre: ")
for caracter in cadena:
    Contador_de_caracteres += 1
    print(f"{caracter}",end = "-")
print()
print(Contador_de_caracteres)

#Ejemplo 1
alumnos = ["Rosalinda","Juan","Lourdes","Tania","Bryan","Rebeca","Jennifer","Hector","Galilea","Patricia","Jesús","Addi"]
for alumno in alumnos:
    print(f"Hola {alumno}.")

for i in range (1,10):
    prinyhyt(i)

