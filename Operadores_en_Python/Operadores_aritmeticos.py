#Galilea Peralta Contreras.
#15 de octubre de 2024.
#Descripción:
#Ejemplos de uso de los operadores aritméticos.

"""
Los operadores aritméticos en Python son los siguientes:
- Suma (+).
- Resta (-).
- Multiplicación (*).
- División (/).
- División entera (//).
- Módulo (%).
- Exponenciación (**).
"""

#Se solicitan dos números enteros al usuario.
Variable_1 = input("Ingrese un número: ")
Variable_1 = int(Variable_1)

Variable_2 = input("Ingrese un número: ")
Variable_2 = int(Variable_2)

#Se realizan las operaciones aritméticas.

#Suma.
print(f"El número {Variable_1} con {Variable_2} da como resultado {Variable_1 + Variable_2}")

#Resta.
print(f"El número {Variable_1} con {Variable_2} da como resultado {Variable_1 - Variable_2}")

#Multiplicación.
print(f"El número {Variable_1} con {Variable_2} da como resultado {Variable_1 * Variable_2}")

#División.
# El formato :.2f limita el resultado a dos decimales.
print(f"El número {Variable_1} con {Variable_2} da como resultado {Variable_1 / Variable_2:.2f}")

#Exponenciación.
print(f"El número {Variable_1} con {Variable_2} da como resultado {Variable_1 ** Variable_2}")

#División entera.
#Devuelve solo la parte entera del cociente.
print(f"El número {Variable_1} con {Variable_2} da como resultado {Variable_1 // Variable_2}")

