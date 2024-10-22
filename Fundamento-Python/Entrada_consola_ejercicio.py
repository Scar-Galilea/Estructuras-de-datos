#Galilea Peralta Contreras.
#14 de octubre de 2024.
#Descripción:
#Ejercicios.

#Escribe un programa de nombre Entrada_consola_ejercicio.py que realice lo siguiente:
#a) Pida 2 números decimales por consola al usuario utilizando la función input.
Variable_1 = input("Ingrese un número decimal: ")
Variable_2 = input("Ingrese un número decimal: ")

#Convertir la cadena a número decimal.
# Esto es necesario para poder realizar operaciones aritméticas con los valores ingresados.
Variable_1 = float(Variable_1)
Variable_2 = float(Variable_2)

#b) Muestre los resultados de las operaciones básicas con esos números: suma, resta, multiplicación y división.
print()
print(f"El número {Variable_1} y {Variable_2} dan como resultado: {Variable_1 + Variable_2}")
print(f"El número {Variable_1} y {Variable_2} dan como resultado: {Variable_1 - Variable_2}")
print(f"El número {Variable_1} y {Variable_2} dan como resultado: {Variable_1 * Variable_2}")
print(f"El número {Variable_1} y {Variable_2} dan como resultado: {Variable_1 / Variable_2}")