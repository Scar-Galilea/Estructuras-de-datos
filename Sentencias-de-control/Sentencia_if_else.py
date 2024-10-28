#Galilea Peralta Contreras.
#23 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
#Uso de la sentencia de control if-else.

"""
La sentencia if-else es una estructura de control fundamental que permite tomar decisiones en el código.
Dependiendo de si se cumple una determinada condición, el programa tomará un camino u otro.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera.

else:
    # Código a ejecutar si la condición es falsa.

# Código que se ejecuta sin importar la condición.
"""

# Ejemplo en donde se determina si un número es par o impar.
print("*** Programa que determina si un número es par o impar +++")

#Solicitamos el número.
Variable_1 = input("Ingresa un número: ")
Variable_1 = int(Variable_1)


# lógica para determinar si es par o impar.
if Variable_1 %2 == 0:
    print(f"El número {Variable_1} es par ") #Implica que es par.
else:
    print(f"El número {Variable_1} es impar") #Implica que es impar.