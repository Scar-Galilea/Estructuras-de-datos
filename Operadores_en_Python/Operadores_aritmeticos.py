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

# Se solicitan dos números enteros al usuario.
Variable_1 = input("Ingrese un numero: ")
Variable_1 =int(Variable_1)

Variable_2 = input("Ingrese un numero: ")
Variable_2 = int(Variable_2)

# Se realizan las operaciones aritméticas.
print(f"El numero {Variable_1} con {Variable_2} da como resultado {Variable_1 + Variable_2}")
print(f"El numero {Variable_1} con {Variable_2} da como resultado {Variable_1 - Variable_2}")
print(f"El numero {Variable_1} con {Variable_2} da como resultado {Variable_1 * Variable_2}")
print(f"El numero {Variable_1} con {Variable_2} da como resultado {Variable_1 / Variable_2:.2f}")
print(f"El numero {Variable_1} con {Variable_2} da como resultado {Variable_1 ** Variable_2}")
print(f"El numero {Variable_1} con {Variable_2} da como resultado {Variable_1 // Variable_2}")

