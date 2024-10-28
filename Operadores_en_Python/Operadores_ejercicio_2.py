#Galilea Peralta Contreras.
#16 de octubre de 2024.
#Descripción:
#Comunidad de la UNSIJ

#Escribe un programa de nombre Operadores_ejercicio2.py que realice lo siguiente:
#Este programa determinará si una persona forma parte de la comunidad de la UNSIJ. Para ello:
#a) Pregunte al usuario si es profesor de la UNSIJ (Si/No).
#b) Pregunte al usuario si es alumno de la UNSIJ (Si/No).
#c) La persona forma parte de la UNSIJ si es profesor o alumno de la UNSIJ.
#d) Muestre el resultado en consola como valor booleano (True/False).

print("*** Comunidad de la UNSIJ ***")
Variable_1 = input("¿Es profesor de la UNSIJ? ")
Variable_2 = input("Es estudiante de la UNSIJ? ")

Expresión_1 = Expresión_1.lower()=="si"
Expresión_2 = Expresión_2.lower()=="si"

# Imprimimos el resultado final: será True si cumple alguna de las condiciones (profesor o estudiante).
print(f"¿Formas parte de la comunidad  UNSIJ? {Variable_1 or Variable_2}")