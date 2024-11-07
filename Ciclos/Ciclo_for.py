

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
    print(i)

