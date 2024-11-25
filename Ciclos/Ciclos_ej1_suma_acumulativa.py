#Galilea Peralta Contreras.
#28 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.

"""
Escribe un programa de nombre Ciclos_ej1_suma_acumulativa.py que realice lo siguiente:

Este programa calculará la suma acumulativa del cero hasta un número ingresado por el usuario. Para ello:

a) Solicite al usuario un número mayor a cero que será el número hasta donde se realizará la suma.

b) Calcule la suma acumulativa.

c) Muestre el resultado de la suma.
"""
print("*** Programa que calcula la suma acumulativa **+")
Variable_1 = input("Ingrese el número final: ")
Variable_1 = int(Variable_1)


Contador_1 = 0
Total = 0

while Contador_1 <= Variable_1 :
    Total += Contador_1
    Contador_1 += 1
print()
print(f"La suma del 0 al {Variable_1} son: ")
print(Total)

