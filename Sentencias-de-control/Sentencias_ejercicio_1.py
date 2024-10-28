#Galilea Peralta Contreras.
#28 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
#Ejercicio

"""
Escribe un programa de nombre Sentencias_ejercicio1.py que realice lo siguiente:

Este programa determinará cuál de dos números ingresados por el usuario es menor o si son iguales. Para ello:

a) Solicite al usuario dos números decimales.

b) Utilice la lógica adecuada para determinar cuál de los dos números es menor o si es que son iguales.

c) Muestre el número menor (o que son iguales) en consola.
"""

print("*** Programa que determine cual numero es menor o si son iguales. ***")
Variable_1 = input("Ingrese número: ")
Variable_2 = input("Ingrese otro número: ")

Variable_1 = float(Variable_1)
Variable_2 = float(Variable_2)

if Variable_1 < Variable_2:
    print(f"El nùmero {Variable_1} es menor que {Variable_2}")
elif Variable_1 > Variable_2:
    print(f"El nùmero {Variable_2} es menor que {Variable_1}")
else:
    print(f"El nùmero {Variable_1} es igual que {Variable_2}")